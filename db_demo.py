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
for key in info.keys():
    value = info[key]
    if isinstance(value, list):
        info[key] = ",".join(value)
param = (id, info["director_id"], info["screenwriter_id"], info["actor_id"], info["类型"],
         info["制片国家/地区"], info["语言"], info["上映日期"], info["rating"], info["rating_count"],
         info["rating_weight"])
query = "INSERT INTO `movie` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
cur.execute(query, param)
conn.commit()
cur.close()
conn.close()