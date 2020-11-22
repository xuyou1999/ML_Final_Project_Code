from requests_html import HTMLSession


class DoubanAPI:
    def __init__(self):
        self.session = HTMLSession()
        self.id = None
        self.data = None

    def search(self, id):
        self.id = str(id)
        url = "https://movie.douban.com/subject/" + str(id)
        self.data = self.session.get(url).html

    def info(self):
        data = self.data
        if not data:
            raise Exception("Please search first!")
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

        info_dict.update(rating_dict)
        return info_dict

    def __str__(self):
        return self.id


if __name__ == '__main__':
    D = DoubanAPI()
    D.search(6828945)
    print(D.info())
    print(D)
