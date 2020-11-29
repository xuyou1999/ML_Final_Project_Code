import pymysql
from DoubanAPI import DoubanAPI

conn = pymysql.connect(host="localhost", user="root", password="", port=3306, database="movie_info", charset="utf8")
cur = conn.cursor()
d = DoubanAPI()
id = 30220799
try:
    d.search(id)
except IndexError:
    print("invalid movie!")
info = d.info()
param = (id, str(info["director_id"]), str(info["screenwriter_id"]), str(info["actor_id"]), str(info["类型"]),
         str(info["制片国家/地区"]), str(info["语言"]), str(info["上映日期"]), info["rating"], info["rating_count"],
         str(info["rating_weight"]))
query = "INSERT INTO `movie` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cur.execute(query, param)
conn.commit()
cur.close()
conn.close()