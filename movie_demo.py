import json
from requests import Session

s = Session()
ip_pool = [
    '119.98.44.192:8118',
    '111.198.219.151:8118',
    '101.86.86.101:8118',
]
proxy_pool = [ip + 'http://' for ip in ip_pool]
start = 0
proxy_num = 0
proxies = {'http':proxy_pool[proxy_num]}
while True:
    url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=" + str(start) + \
          "&year_range=2010,2019"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/60.0.3100.0 Safari/537.36"}
    response = s.get(url, headers=headers, proxies=proxies)
    try:
        data = json.loads(response.text)["data"]
    except KeyError:
        proxy_num += 1
        continue
    for movie in data:
        id = movie["id"]
        with open("movie.txt", 'a') as file:
            file.write(id + "\n")
    start += 20