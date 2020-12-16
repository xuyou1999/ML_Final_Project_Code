import time

from DoubanAPI import DoubanAPI
from db_class import MyDb
from logger_class import Logger


def create_db(db):
    """
    warning: calling this function will automatically drop database "movie_info", unless modify "create_db.sql"

    :param db: MyDb object
    """
    with open('create_db.sql', encoding='utf-8', mode='r') as f:
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            if '\n' in x:
                x = x.replace('\n', ' ')
            if '    ' in x:  # replace multiple space with empty string
                x = x.replace('    ', '')
            sql_item = x + ';'
            db.execute(sql_item)


def filter_data(db):
    """
    filter out movie data in database where there is no date for that movie

    :param db: MyDb object
    """
    query = "DELETE FROM `actor_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `director_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `writer_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `genre_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `language_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `region_movie` WHERE movie_ID IN (SELECT ID FROM `movie` WHERE date = '')"
    db.execute(query)
    query = "DELETE FROM `movie` WHERE date = ''"
    db.execute(query)


def extract_data():
    # load id data
    file = open("movie.txt", "r")
    id_list = file.readlines()
    for i in range(len(id_list)):
        id_list[i] = id_list[i].strip("\n")

    # setup
    logger = Logger("file").getLogger()

    with MyDb("localhost", "root", "", 3306) as db, DoubanAPI() as D:
        # create database "movie_info", comment this block if database already created
        try:
            create_db(db)
        except Exception as e:
            logger.error(e)
            raise Exception("Database creation failed!")

        # connect to "movie_info"
        db.connect_to_db("movie_info")

        # begin extraction and insertion
        for id in id_list:
            time.sleep(3)  # simulate user behaviour
            # extraction
            try:
                D.search(id)
                logger.info("Search success for id: " + str(id))
            except Exception as e:  # error caused by ip ban
                logger.error(e)
                raise Exception("Ip banned!")
            try:
                info = d.info()
            except Exception as e:  # error caused by ip ban
                logger.error(e)
                raise Exception("Ip banned!")

            # insert into entity 'movie'
            query = "INSERT INTO `movie` VALUES (%s, %s, %s, %s, %s)"
            param = (id, ",".join(info["上映日期"]), info["rating"], info["rating_count"], ",".join(info["rating_weight"]))
            try:
                db.execute(query, param)
            except Exception as e:  # error caused by duplicate id in txt
                logger.error(e)
                logger.info("Failure in id: " + str(id))
                continue

            # insert into relations
            query = "INSERT INTO `director_movie` VALUES (%s, %s)"
            for d in info["director_id"]:
                try:
                    param = (d, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `actor_movie` VALUES (%s, %s)"
            for a in info["actor_id"]:
                try:
                    param = (a, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `writer_movie` VALUES (%s, %s)"
            for w in info["screenwriter_id"]:
                try:
                    param = (w, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `actor_movie` VALUES (%s, %s)"
            for a in info["actor_id"]:
                try:
                    param = (a, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `genre_movie` VALUES (%s, %s)"
            for g in info["类型"]:
                try:
                    param = (g, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `region_movie` VALUES (%s, %s)"
            for r in info["制片国家/地区"]:
                try:
                    param = (r, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            query = "INSERT INTO `language_movie` VALUES (%s, %s)"
            for l in info["语言"]:
                try:
                    param = (l, id)
                    db.execute(query, param)
                except Exception as e:
                    logger.error(e)
                    continue
            # if success
            logger.info("Success in id: " + str(id))
        logger.info("Finish insertion")

        time.sleep(3000)  # wait until insertion finish successfully
        filter_data(db)


# please use valid proxy pool for DoubanAPI (modify in DoubanAPI.py)
if __name__ == '__main__':
    extract_data()
