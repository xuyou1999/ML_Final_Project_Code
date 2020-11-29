import pymysql
from DoubanAPI import DoubanAPI

# process data
file = open("movie.txt", "r")
id_list = file.readlines()
for i in range(len(id_list)):
    id_list[i] = id_list[i].strip("\n")
print(id_list)

# setup
conn = pymysql.connect(host="localhost", user="root", password="", port=3306, database="movie_info", charset="utf8")
cur = conn.cursor()
d = DoubanAPI()

# close
cur.close()
conn.close()