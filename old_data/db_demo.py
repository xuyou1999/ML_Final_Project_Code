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

query = "INSERT INTO `movie` VALUES (%s, %s, %s, %s, %s)"
param = (id, ",".join(info["上映日期"]), info["rating"], info["rating_count"], ",".join(info["rating_weight"]))
cur.execute(query, param)

query = "INSERT INTO `director_movie` VALUES (%s, %s)"
for d in info["director_id"]:
    try:
        param = (d, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `actor_movie` VALUES (%s, %s)"
for a in info["actor_id"]:
    try:
        param = (a, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `writer_movie` VALUES (%s, %s)"
for w in info["screenwriter_id"]:
    try:
        param = (w, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `actor_movie` VALUES (%s, %s)"
for a in info["actor_id"]:
    try:
        param = (a, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `genre_movie` VALUES (%s, %s)"
for g in info["类型"]:
    try:
        param = (g, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `region_movie` VALUES (%s, %s)"
for r in info["制片国家/地区"]:
    try:
        param = (r, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

query = "INSERT INTO `language_movie` VALUES (%s, %s)"
for l in info["语言"]:
    try:
        param = (l, id)
        cur.execute(query, param)
    except Exception as e:
        print(e)
        continue

conn.commit()
cur.close()
conn.close()