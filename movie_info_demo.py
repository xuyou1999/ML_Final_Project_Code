from requests_html import HTMLSession

s = HTMLSession()
data = s.get("https://movie.douban.com/subject/30220799/")  # 冷门：6828945  热门：30220799
info = data.html.find("div#info", first=True)
info_text = info.text.split("\n")
info_list = [i.split(": ") for i in info_text]
info_dict = {i[0]: i[1].split(" / ") for i in info_list}
# attr_list = info.find("span.attrs")
# director = attr_list[0]
# director_name = director.text.split(" / ")
actor_index = 2
try:
    director_name = info_dict["导演"]
except KeyError:
    director_name = None
    actor_index -= 1
try:
    screenwriter_name = info_dict["编剧"]
except KeyError:
    screenwriter_name = None
    actor_index -= 1
print("Director:", director_name)
# screenwriter = attr_list[1]
# screenwriter_name = screenwriter.text.split(" / ")
print("Screenwriter:", screenwriter_name)


# actor_name = actor.text.split(" / ")
try:
    actor_name = info_dict["主演"]
    attr_list = info.find("span.attrs")
    actor = attr_list[actor_index]
    actor_attr = actor.find("a")
    actor_href = [a.attrs["href"] for a in actor_attr]
    actor_url = ["movie.douban.com" + href for href in actor_href]
except KeyError:
    actor_name = None
print("Actor Href:", actor_href)
print("Actor URL:", actor_url)
print("Actors:", actor_name)

rate = data.html.find("div.rating_self", first=True)
rating_info = rate.text.split("\n")
rating = rating_info[0]
rating_count = rating_info[1]
print("Rating:", rating)
print("Rating Counts:", rating_count)
weight = data.html.find("div.ratings-on-weight", first=True)
weight_info = weight.text.split("\n")
rating_weight = [weight_info[i] for i in [1, 4, 7, 10, 13]]
print("Rating Weights (5, 4, 3, 2, 1 star[s]):", rating_weight)
