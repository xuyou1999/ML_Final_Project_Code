import json
import time

from requests_html import HTMLSession


class DoubanAPI:

    def __init__(self):
        self.session = HTMLSession()
        self.id = None
        self.data = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        if exc_tb or exc_type or exc_val:
            print(exc_type, exc_type, exc_val)
        return True  # do not throw exception if exception occurs in with clause

    def search(self, id):
        self.id = str(id)
        url = "https://movie.douban.com/subject/" + str(id)
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/60.0.3100.0 Safari/537.36"}
        proxies = {
            "http": "http://49.71.141.225:13456"
        }
        try:
            self.data = self.session.get(url, headers=headers).html
        except Exception as e:
            print(e)

    def info(self):
        data = self.data
        if not data:
            raise Exception("Please search for data first!")

        # handle error in other program
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

    def find_id(self, is_sorted=False, tags="电影", start=0, year_range=(2010, 2019), outpath=None, max_num=100):
        s = "U" if not is_sorted else "T"
        r = str(year_range[0]) + "," + str(year_range[1])
        out = outpath if outpath else "movie_id.txt"
        file = open(out, 'a')
        session = self.session
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/60.0.3100.0 Safari/537.36"}
        while start < max_num:
            url = "https://movie.douban.com/j/new_search_subjects?sort=" + s + "&range=0,10&tags=" + tags + \
                  "&start=" + str(start) + "&year_range=" + r
            start += 20
            try:
                response = session.get(url, headers=headers)
                data = json.loads(response.text)["data"]
            except Exception as e:
                print(e)
                continue
            for movie in data:
                id = movie["id"]
                file.write(id + "\n")
            time.sleep(3)  # simulate user behaviour
        file.close()


if __name__ == '__main__':
    with DoubanAPI() as D:
        D.search(30220799)
        print(D.info())
        # D.find_id()
