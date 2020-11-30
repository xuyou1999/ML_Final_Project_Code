import pymysql
from pymysql.cursors import *
import csv


class MyDb:
    def __init__(self, host, user, passwd, port, db_name=None, charset="utf8", autocommit=True):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.db_name = db_name
        self.charset = charset
        self.autocommit = autocommit
        self.conn = None
        self.cur = None

    def __enter__(self):  # usage: with MyDb(param) as db
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port,
                                        database=self.db_name, charset=self.charset, autocommit=self.autocommit)
            self.cur = self.conn.cursor(Cursor)
        except Exception as e:
            print(e)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()

    def connect_to_db(self, db_name):
        self.db_name = db_name
        return self.__enter__()

    def set_cursor(self, cursor_type=Cursor):
        try:
            self.cur = self.conn.cursor(cursor_type)
        except Exception as e:
            print(e)

    def execute(self, query, param=None, commit=True):
        try:
            self.cur.execute(query, param)
        except Exception as e:
            print(e)
        if commit and not self.autocommit:
            self.conn.commit()

    def executemany(self, query, param=None, commit=True):
        try:
            self.cur.executemany(query, param)
        except Exception as e:
            print(e)
        if commit and not self.autocommit:
            self.conn.commit()

    def fetchone(self):  # For details, visit https://blog.csdn.net/qq_44421796/article/details/105643697
        try:
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def fetchall(self):
        try:
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def fetchmany(self):
        try:
            return self.cur.fetchmany()
        except Exception as e:
            print(e)

    def execute_to_csv(self, query, outpath=None, param=None):
        try:
            self.execute(query, param)
            data = self.fetchall()
        except Exception as e:
            print(e)
        out = outpath if outpath else "data.csv"
        with open(out, mode='w', encoding='utf-8') as f:
            write = csv.writer(f, dialect='excel')
            for item in data:
                write.writerow(item)


if __name__ == '__main__':
    with MyDb("localhost", "root", "", 3306) as db:
        db.connect_to_db("movie_info")
        query = "insert into `movie` values(%s, %s, %s, %s, %s)"
        db.execute(query, (1, 1, 1, 1, 1))
        query = "select * from `movie` where id = 1"
        db.execute(query)
        result = db.fetchone()
        print("After Insertion:", result)
        query = "delete from `movie` where id = 1"
        db.execute(query)
        query = "select * from `movie` where id = 1"
        db.execute(query)
        result = db.fetchone()
        print("After Delete:", result)
