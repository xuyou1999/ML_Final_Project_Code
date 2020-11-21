import json
from requests import Session

s = Session()
start = 0
while True:
    url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=" + str(start) + \
          "&year_range=2010,2019"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/60.0.3100.0 Safari/537.36",
               "cookie": 'll="108296"; bid=nWq4k-KjCqs; __gads=ID=8960cdccb618879f-22096d33d9c400a2:T=1605890801:'
                         'S=ALNI_MZs12Yi9DWxDKkzX6j2HOHI7MFs0g; _vwo_uuid_v2=D7E2B615C39991E6F355FAF8BC49E04B5|'
                         '1628d95d7afc0e4bde5178d8d491828e; __yadk_uid=mdzcqHNcFJ4oUuUh9lmlBYh6yHwAvxPL; '
                         'ct=y; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; __utmt=1; _pk_ref.100001.4cf6='
                         '%5B%22%22%2C%22%22%2C1605968634%2C%22https%3A%2F%2Fsearch.douban.com%2Fmovie%2Fsubject'
                         '_search%3Fsearch_text%3D2013%26cat%3D1002%22%5D; _pk_ses.100001.4cf6=*; dbcl2="227039831:'
                         'ndjXF9XXanI"; ck=dq-K; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22703; __utma='
                         '30149280.337909721.1605890754.1605966684.1605968719.9; __utmz=30149280.1605968719.9.3.'
                         'utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=223695111.'
                         '1291400405.1605890799.1605968634.1605968719.8; __utmz=223695111.1605968719.8.4.utmcsr='
                         'google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=30149280.2.10.'
                         '1605968719; __utmb=223695111.4.10.1605968719; _pk_id.100001.4cf6=3af7068fc90bbf9d.'
                         '1605890799.7.1605968741.1605964410.'}
    response = s.get(url, headers=headers)
    data = json.loads(response.text)["data"]
    for movie in data:
        id = movie["id"]
        with open("movie.txt", 'a') as file:
            file.write(id + "\n")
    start += 20