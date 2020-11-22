from requests_html import HTMLSession

s = HTMLSession()

ID = "25820460"  # 冷门：6828945  热门：30220799
data = s.get("https://movie.douban.com/subject/" + ID + "/")
info = data.html.find("div#info", first=True)
info_text = info.text.split("\n")
info_list = [i.split(": ") for i in info_text]
info_dict = {i[0]: i[1].split(" / ") for i in info_list}
attr_list = info.find("span.attrs")

director_index = 0
screenwriter_index = 1
actor_index = 2

try:
    director_name = info_dict["导演"]
    director = attr_list[director_index]
    director_attr = director.find("a")
    director_href = [d.attrs["href"] for d in director_attr]
except KeyError:
    director_name = None
    director_href = None
    screenwriter_index -= 1
    actor_index -= 1

try:
    screenwriter_name = info_dict["编剧"]
    screenwriter = attr_list[screenwriter_index]
    screenwriter_attr = screenwriter.find("a")
    screenwriter_href = [s.attrs["href"] for s in screenwriter_attr]
except KeyError:
    screenwriter_name = None
    screenwriter_href = None
    actor_index -= 1

print("Director Name:", director_name)
print("Director Href:", director_href)

print("Screenwriter Name:", screenwriter_name)
print("Screenwriter Href:", screenwriter_href)

try:
    actor_name = info_dict["主演"]
    actor = attr_list[actor_index]
    actor_attr = actor.find("a")
    actor_href = [a.attrs["href"] for a in actor_attr]
    actor_url = ["movie.douban.com" + href for href in actor_href]
except KeyError:
    actor_name = None
    actor_href = None
    actor_url = None

print("Actor Names:", actor_name)
print("Actor Href:", actor_href)
print("Actor URL:", actor_url)


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

print(info_dict)