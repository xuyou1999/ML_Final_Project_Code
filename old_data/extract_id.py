from DoubanAPI import DoubanAPI


if __name__ == '__main__':
    data_size = 3000
    out = "movie.txt"
    with DoubanAPI() as D:
        D.find_id(False, "电影", 0, (2010, 2019), out, data_size)
