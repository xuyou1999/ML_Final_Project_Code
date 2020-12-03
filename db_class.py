import csv

import pymysql
from pymysql.cursors import *


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
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port,
                                    database=self.db_name, charset=self.charset, autocommit=self.autocommit)
        self.cur = self.conn.cursor(Cursor)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()
        if exc_tb or exc_type or exc_val:
            print(exc_type, exc_type, exc_val)
        return True  # do not throw exception if exception occurs in with clause

    def connect(self):
        return self.__enter__()

    def connect_to_db(self, db_name):
        self.db_name = db_name
        return self.__enter__()

    def set_cursor_type(self, cursor_type=Cursor):
        if not self.cur:
            raise Exception("Please connect first!")
        self.cur = self.conn.cursor(cursor_type)

    def execute(self, query, param=None, commit=None):
        commit = self.autocommit if commit is None else commit
        try:
            return self.cur.execute(query, param)
        except Exception as e:
            print(e)
            self.conn.rollback()
        if commit and not self.autocommit:
            self.conn.commit()

    def executemany(self, query, param=None, commit=None):
        commit = self.autocommit if commit is None else commit
        try:
            return self.cur.executemany(query, param)
        except Exception as e:
            print(e)
            self.conn.rollback()
        if commit and not self.autocommit:
            self.conn.commit()

    def fetchone(self):  # For details, visit https://blog.csdn.net/qq_44421796/article/details/105643697
        return self.cur.fetchone()

    def fetchall(self):
        return self.cur.fetchall()

    def fetchmany(self):
        return self.cur.fetchmany()

    def execute_to_csv(self, query, param=None, outpath=None, header=None):
        self.execute(query, param)
        data = self.fetchall()
        out = outpath if outpath else str(hash(query)) + ".csv"
        f = open(out, mode='w', encoding='utf-8', newline='')
        write = csv.writer(f, dialect='excel')
        if header:
            write.writerow(header)
        for item in data:
            write.writerow(item)
        f.close()


if __name__ == '__main__':
    with MyDb("localhost", "root", "", 3306) as db:
        db.connect_to_db("movie_info")
        db.set_cursor_type(DictCursor)
        query = "insert into `movie` values(%s, %s, %s, %s, %s)"
        db.execute(query, (1, 1, 1, 1, 1))
        query = "select * from `movie` where id = 1"
        db.execute(query)
        result = db.fetchall()
        print("After Insertion:", result)
        query = "delete from `movie` where id = 1"
        row_count = db.execute(query)
        print("Affected %d row(s)" % row_count)
        query = "select * from `movie` where id = 1"
        db.execute(query)
        result = db.fetchone()
        print("After Deletion:", result)
