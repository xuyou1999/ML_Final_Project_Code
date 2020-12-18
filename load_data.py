'''
Works Cited
豆瓣电影. https://movie.douban.com/. Accessed Dec. 2020.
'''

import os

from db_class import MyDb
from logger_class import Logger
from extract_data import filter_data


def make_dir():
    if not os.path.exists("./data"):
        os.mkdir("./data")


def get_movie(db):
    header = ("movie_id", "date", "movie_rating", "rating_count", "rating_weight")
    query = "select * from `movie`"
    db.execute_to_csv(query, None, "./data/movie.csv", header)


def actor_info(db):
    header = ("actor_id", "movie_count", "avg_rating")
    query = "SELECT actor_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `actor_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY actor_id "
    db.execute_to_csv(query, None, "./data/actor_avg.csv", header)
    header = ("movie_id", "actor_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN actor_movie JOIN (SELECT actor_ID, COUNT(movie_ID) " \
            "AS movie_count, AVG(rating) AS avg_r FROM `actor_movie` JOIN movie WHERE movie_ID = ID GROUP BY " \
            "actor_ID) AS T WHERE ID = actor_movie.movie_ID AND actor_movie.actor_ID = T.actor_ID GROUP BY ID "
    db.execute_to_csv(query, None, "./data/actor_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM actor_movie)"
    db.execute_to_csv(query, None, "./data/actor_empty.csv", header)


def director_info(db):
    header = ("director_id", "movie_count", "avg_rating")
    query = "SELECT director_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `director_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY director_id "
    db.execute_to_csv(query, None, "./data/director_avg.csv", header)
    header = ("movie_id", "director_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN director_movie JOIN (SELECT director_ID, " \
            "COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_r FROM `director_movie` JOIN movie WHERE movie_ID = " \
            "ID GROUP BY director_ID) AS T WHERE ID = director_movie.movie_ID AND director_movie.director_ID = " \
            "T.director_ID GROUP BY ID "
    db.execute_to_csv(query, None, "./data/director_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM director_movie)"
    db.execute_to_csv(query, None, "./data/director_empty.csv", header)


def writer_info(db):
    header = ("writer_id", "movie_count", "avg_rating")
    query = "SELECT writer_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `writer_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY writer_id "
    db.execute_to_csv(query, None, "./data/writer_avg.csv", header)
    header = ("movie_id", "writer_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN writer_movie JOIN (SELECT writer_ID, COUNT(movie_ID) " \
            "AS movie_count, AVG(rating) AS avg_r FROM `writer_movie` JOIN movie WHERE movie_ID = ID GROUP BY " \
            "writer_ID) AS T WHERE ID = writer_movie.movie_ID AND writer_movie.writer_ID = T.writer_ID GROUP BY ID "
    db.execute_to_csv(query, None, "./data/writer_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM writer_movie)"
    db.execute_to_csv(query, None, "./data/writer_empty.csv", header)


def genre_info(db):
    header = ("genre", "movie_count", "avg_rating")
    query = "SELECT genre, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `genre_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY genre "
    db.execute_to_csv(query, None, "./data/genre_avg.csv", header)
    header = ("movie_id", "genre_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN genre_movie JOIN (SELECT genre, COUNT(movie_ID) AS " \
            "movie_count, AVG(rating) AS avg_r FROM `genre_movie` JOIN movie WHERE movie_ID = ID GROUP BY genre) AS " \
            "T WHERE ID = genre_movie.movie_ID AND genre_movie.genre = T.genre GROUP BY ID "
    db.execute_to_csv(query, None, "./data/genre_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM genre_movie)"
    db.execute_to_csv(query, None, "./data/genre_empty.csv", header)


def language_info(db):
    header = ("language", "movie_count", "avg_rating")
    query = "SELECT language, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `language_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY language "
    db.execute_to_csv(query, None, "./data/language_avg.csv", header)
    header = ("movie_id", "language_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN language_movie JOIN (SELECT language, " \
            "COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_r FROM `language_movie` JOIN movie WHERE movie_ID = " \
            "ID GROUP BY language) AS T WHERE ID = language_movie.movie_ID AND language_movie.language = T.language " \
            "GROUP BY ID "
    db.execute_to_csv(query, None, "./data/language_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM language_movie)"
    db.execute_to_csv(query, None, "./data/language_empty.csv", header)


def region_info(db):
    header = ("region", "movie_count", "avg_rating")
    query = "SELECT region, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `region_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY region "
    db.execute_to_csv(query, None, "./data/region_avg.csv", header)
    header = ("movie_id", "region_rating")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN region_movie JOIN (SELECT region, COUNT(movie_ID) AS " \
            "movie_count, AVG(rating) AS avg_r FROM `region_movie` JOIN movie WHERE movie_ID = ID GROUP BY region) AS " \
            "T WHERE ID = region_movie.movie_ID AND region_movie.region = T.region GROUP BY ID "
    db.execute_to_csv(query, None, "./data/region_pred_avg.csv", header)
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM region_movie)"
    db.execute_to_csv(query, None, "./data/region_empty.csv", header)


if __name__ == '__main__':
    logger = Logger("file").getLogger()
    make_dir()
    with MyDb("localhost", "root", "", 3306, "movie_info") as db:
        filter_data(db)
        try:
            get_movie(db)
            actor_info(db)
            director_info(db)
            writer_info(db)
            genre_info(db)
            language_info(db)
            region_info(db)
        except Exception as e:
            logger.error(e)
