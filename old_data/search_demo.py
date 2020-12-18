import asyncio

from lxml import etree
from pyppeteer import launch

key_word = "indo"
opt = {
    "ignoreHTTPSErrors": True,
    "headless": False,
    'userDataDir': r'D:\temp',  # path for temporary data
    "args": ['--no-sandbox', "--disable-infobars"]
}


def process(cont):
    document = etree.HTML(cont)
    source_list = document.xpath("//a")
    celeb_file = open("celeb_data.txt", 'a')
    movie_file = open("movie_data.txt", 'a')
    celeb = []
    movie = []
    for s in source_list:
        link = s.attrib["href"]
        if "movie.douban.com/celebrity" in link:
            celeb.append(link.split("/")[-2])
        elif "movie.douban.com/subject" in link:
            movie.append(link.split("/")[-2])
    celeb = list(set(celeb))
    movie = list(set(movie))
    celeb.append(key_word)
    movie.append(key_word)
    celeb_file.write(str(celeb) + "\n")
    movie_file.write(str(movie) + "\n")


async def main(url):
    browser = await launch(opt)
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(url, {"waitUntil": "networkidle2"})
    content = await page.content()
    process(content)
    await page.close()
    await browser.close()


if __name__ == '__main__':
    start = 0
    url = "https://search.douban.com/movie/subject_search?search_text=" + key_word + "&cat=1002&start=" + str(start)
    try:
        asyncio.get_event_loop().run_until_complete(main(url))
    except Exception as e:
        print(e)
