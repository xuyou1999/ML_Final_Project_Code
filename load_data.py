from db_class import MyDb
from logger_class import Logger


def get_movie(db):
    query = "select * from `movie`"
    db.execute_to_csv(query, "./data/movie.csv")


def actor_avg(db):
    query = "SELECT actor_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `actor_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY actor_id "
    db.execute_to_csv(query, "./data/actor_avg.csv")


def director_avg(db):
    query = "SELECT director_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `director_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY director_id "
    db.execute_to_csv(query, "./data/director_avg.csv")


def writer_avg(db):
    query = "SELECT writer_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `writer_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY writer_id "
    db.execute_to_csv(query, "./data/writer_avg.csv")


def genre_avg(db):
    query = "SELECT genre, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `genre_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY genre "
    db.execute_to_csv(query, "./data/genre_avg.csv")


def language_avg(db):
    query = "SELECT language, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `language_movie` JOIN " \
            "movie WHERE movie_ID = ID GROUP BY language "
    db.execute_to_csv(query, "./data/language_avg.csv")


def region_avg(db):
    query = "SELECT region, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `region_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY region "
    db.execute_to_csv(query, "./data/region_avg.csv")


if __name__ == '__main__':
    logger = Logger("file").getLogger()
    with MyDb("localhost", "root", "", 3306, "movie_info") as db:
        try:
            get_movie(db)
            actor_avg(db)
            director_avg(db)
            writer_avg(db)
            genre_avg(db)
            language_avg(db)
            region_avg(db)
        except Exception as e:
            logger.error(e)
