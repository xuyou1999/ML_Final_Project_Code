import asyncio
from pyppeteer import launch
from lxml import etree

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
    celeb_file.write(key_word + "\n")
    movie_file.write(key_word + "\n")
    for s in source_list:
        link = s.attrib["href"]
        if "movie.douban.com/celebrity" in link:
            celeb_file.write(link.split("/")[-2] + "\n")
        elif "movie.douban.com/subject" in link:
            movie_file.write(link.split("/")[-2] + "\n")


async def main(url):
    browser = await launch(opt)
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto(url, {"waitUntil": "networkidle2"})
    content = await page.content()
    process(content)
    await page.close()


if __name__ == '__main__':
    start = 0
    url = "https://search.douban.com/movie/subject_search?search_text=" + key_word + "&cat=1002&start=" + str(start)
    try:
        asyncio.get_event_loop().run_until_complete(main(url))
    except Exception as e:
        print(e)

