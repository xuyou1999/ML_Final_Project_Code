from requests_html import HTMLSession
from fake_useragent import UserAgent

class DoubanAPI:
    def __init__(self):
        self.session = HTMLSession()
        self.id = None
        self.data = None

    def search(self, id):
        self.id = str(id)
        url = "https://movie.douban.com/subject/" + str(id)
        ua = UserAgent().random
        header = {"User-Agent": ua,
                  "Cookie": 'll="108296"; bid=nWq4k-KjCqs; __gads=ID=8960cdccb618879f-22096d33d9c400a2:T=1605890801:S'
                            '=ALNI_MZs12Yi9DWxDKkzX6j2HOHI7MFs0g; '
                            '_vwo_uuid_v2=D7E2B615C39991E6F355FAF8BC49E04B5|1628d95d7afc0e4bde5178d8d491828e; ct=y; '
                            'push_noty_num=0; push_doumail_num=0; __utmv=30149280.22703; '
                            '__utmz=30149280.1605968719.9.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=('
                            'not%20provided); dbcl2="227039831:0I/Ve4j29Z0"; ck=MUEL; '
                            'frodotk="984a7362e065950fc8df5a28a130bf2d"; ap_v=0,'
                            '6.0; __utma=30149280.337909721.1605890754.1606637790.1606649834.13; '
                            '__utmb=30149280.0.10.1606649834; __utmc=30149280',
                  }
        proxies = {
            "http": "http://49.71.141.225:13456"
        }
        self.data = self.session.post(url, headers=header, proxies=proxies).html

    def info(self):
        data = self.data
        if not data:
            raise Exception("Please search for data first!")
        info = data.find("div#info", first=True)
        info_text = info.text.split("\n")
        info_list = [i.split(": ") for i in info_text]
        info_dict = {i[0]: i[1].split(" / ") for i in info_list}

        attr_list = info.find("span.attrs")
        director_index = 0
        screenwriter_index = 1
        actor_index = 2
        try:
            info_dict["导演"]
            director = attr_list[director_index]
            director_attr = director.find("a")
            director_href = [d.attrs["href"] for d in director_attr]
            director_id = [h.split("/")[-2] for h in director_href]
        except KeyError:
            director_id = []
            screenwriter_index -= 1
            actor_index -= 1
        try:
            info_dict["编剧"]
            screenwriter = attr_list[screenwriter_index]
            screenwriter_attr = screenwriter.find("a")
            screenwriter_href = [s.attrs["href"] for s in screenwriter_attr]
            screenwriter_id = [h.split("/")[-2] for h in screenwriter_href]
        except KeyError:
            screenwriter_id = []
            actor_index -= 1
        try:
            info_dict["主演"]
            actor = attr_list[actor_index]
            actor_attr = actor.find("a")
            actor_href = [a.attrs["href"] for a in actor_attr]
            actor_id = [h.split("/")[-2] for h in actor_href]
        except KeyError:
            actor_id = []
        id_dict = {"director_id": director_id, "screenwriter_id": screenwriter_id, "actor_id": actor_id}
        info_dict.update(id_dict)

        rate = data.find("div.rating_self", first=True)
        rating_info = rate.text.split("\n")
        rating = rating_info[0]
        rating_count = rating_info[1][:-3]
        weight = data.find("div.ratings-on-weight", first=True)
        weight_info = weight.text.split("\n")
        rating_weight = [weight_info[i] for i in [1, 4, 7, 10, 13]]
        rating_dict = {"rating": rating, "rating_count": rating_count, "rating_weight": rating_weight}
        if "类型" not in info_dict.keys():
            info_dict["类型"] = []
        if "上映日期" not in info_dict.keys():
            info_dict["上映日期"] = []
        if "制片国家/地区" not in info_dict.keys():
            info_dict["制片国家/地区"] = []
        if "语言" not in info_dict.keys():
            info_dict["语言"] = []
        info_dict.update(rating_dict)
        return info_dict


if __name__ == '__main__':
    D = DoubanAPI()
    D.search(30220799)
    print(D.info())
