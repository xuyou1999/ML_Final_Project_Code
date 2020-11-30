from db_class import MyDb
from logger_class import Logger


def get_movie(db):
    query = "select * from `movie`"
    db.execute_to_csv(query, "./data/movie.csv")


def actor_info(db):
    query = "SELECT actor_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `actor_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY actor_id "
    db.execute_to_csv(query, "./data/actor_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN actor_movie JOIN (SELECT actor_ID, COUNT(movie_ID) " \
            "AS movie_count, AVG(rating) AS avg_r FROM `actor_movie` JOIN movie WHERE movie_ID = ID GROUP BY " \
            "actor_ID) AS T WHERE ID = actor_movie.movie_ID AND actor_movie.actor_ID = T.actor_ID GROUP BY ID "
    db.execute_to_csv(query, "./data/actor_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM actor_movie)"
    db.execute_to_csv(query, "./data/actor_empty.csv")


def director_info(db):
    query = "SELECT director_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `director_movie` JOIN "\
            "movie WHERE movie_ID = ID GROUP BY director_id "
    db.execute_to_csv(query, "./data/director_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN director_movie JOIN (SELECT director_ID, " \
            "COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_r FROM `director_movie` JOIN movie WHERE movie_ID = " \
            "ID GROUP BY director_ID) AS T WHERE ID = director_movie.movie_ID AND director_movie.director_ID = " \
            "T.director_ID GROUP BY ID "
    db.execute_to_csv(query, "./data/director_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM director_movie)"
    db.execute_to_csv(query, "./data/director_empty.csv")


def writer_info(db):
    query = "SELECT writer_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `writer_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY writer_id "
    db.execute_to_csv(query, "./data/writer_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN writer_movie JOIN (SELECT writer_ID, COUNT(movie_ID) "\
            "AS movie_count, AVG(rating) AS avg_r FROM `writer_movie` JOIN movie WHERE movie_ID = ID GROUP BY " \
            "writer_ID) AS T WHERE ID = writer_movie.movie_ID AND writer_movie.writer_ID = T.writer_ID GROUP BY ID "
    db.execute_to_csv(query, "./data/writer_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM writer_movie)"
    db.execute_to_csv(query, "./data/writer_empty.csv")


def genre_info(db):
    query = "SELECT genre, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `genre_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY genre "
    db.execute_to_csv(query, "./data/genre_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN genre_movie JOIN (SELECT genre, COUNT(movie_ID) AS " \
            "movie_count, AVG(rating) AS avg_r FROM `genre_movie` JOIN movie WHERE movie_ID = ID GROUP BY genre) AS " \
            "T WHERE ID = genre_movie.movie_ID AND genre_movie.genre = T.genre GROUP BY ID "
    db.execute_to_csv(query, "./data/genre_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM genre_movie)"
    db.execute_to_csv(query, "./data/genre_empty.csv")


def language_info(db):
    query = "SELECT language, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `language_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY language "
    db.execute_to_csv(query, "./data/language_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN language_movie JOIN (SELECT language, " \
            "COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_r FROM `language_movie` JOIN movie WHERE movie_ID = " \
            "ID GROUP BY language) AS T WHERE ID = language_movie.movie_ID AND language_movie.language = T.language " \
            "GROUP BY ID "
    db.execute_to_csv(query, "./data/language_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM language_movie)"
    db.execute_to_csv(query, "./data/language_empty.csv")


def region_info(db):
    query = "SELECT region, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `region_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY region "
    db.execute_to_csv(query, "./data/region_avg.csv")
    query = "SELECT ID, AVG(avg_r) AS avg_rating FROM movie JOIN region_movie JOIN (SELECT region, COUNT(movie_ID) AS " \
            "movie_count, AVG(rating) AS avg_r FROM `region_movie` JOIN movie WHERE movie_ID = ID GROUP BY region) AS " \
            "T WHERE ID = region_movie.movie_ID AND region_movie.region = T.region GROUP BY ID "
    db.execute_to_csv(query, "./data/region_pred_avg.csv")
    query = "SELECT ID, rating FROM `movie` WHERE ID NOT IN (SELECT movie_ID FROM region_movie)"
    db.execute_to_csv(query, "./data/region_empty.csv")


if __name__ == '__main__':
    logger = Logger("file").getLogger()
    with MyDb("localhost", "root", "", 3306, "movie_info") as db:
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
