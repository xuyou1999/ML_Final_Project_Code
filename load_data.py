from db_class import MyDb
from logger_class import Logger


def get_movie(db):
    query = "select * from `movie`"
    db.execute_to_csv(query, "./data/movie.csv")


def actor_avg(db):
    query = "SELECT actor_id, COUNT(movie_ID) AS movie_count, AVG(rating) AS avg_rating FROM `actor_movie` JOIN movie " \
            "WHERE movie_ID = ID GROUP BY actor_id "
    db.execute_to_csv(query, "./data/actor_avg.csv")


if __name__ == '__main__':
    logger = Logger("file").getLogger()
    with MyDb("localhost", "root", "", 3306, "movie_info") as db:
        try:
            get_movie(db)
            actor_avg(db)
        except Exception as e:
            logger.error(e)
