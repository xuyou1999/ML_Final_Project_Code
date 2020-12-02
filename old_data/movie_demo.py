import json
from requests import Session
import os

abs_path = os.path.abspath(__file__)
path = os.path.dirname(abs_path)
os.chdir(path)

s = Session()
ip_pool = [
    '119.98.44.192:8118',
    '111.198.219.151:8118',
    '101.86.86.101:8118',
]
proxy_pool = [ip + 'http://' for ip in ip_pool]
start = 7980  # 每次加60
proxy_num = 0
proxy = {'http': "http://113.120.143.234:13456"}
while True:
    url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=电影&start=" + str(start) + \
          "&year_range=2010,2019"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/60.0.3100.0 Safari/537.36"}
    response = s.get(url, headers=headers)
    data = json.loads(response.text)["data"]
    for movie in data:
        id = movie["id"]
        with open("movie.txt", 'a') as file:
            file.write(id + "\n")
    start += 20
