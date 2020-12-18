'''
Works Cited
豆瓣电影. https://movie.douban.com/. Accessed Dec. 2020.
'''

from DoubanAPI import DoubanAPI
from logger_class import Logger


def extract_id():
    data_size = 3000
    out = "movie.txt"
    with DoubanAPI() as D:
        D.find_id(False, "电影", 0, (2010, 2019), out, data_size)


if __name__ == '__main__':
    logger = Logger().getLogger()
    try:
        extract_id()
    except Exception as e:
        logger.error(e)
