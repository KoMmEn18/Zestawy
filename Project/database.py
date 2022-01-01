import sqlite3
import os.path
from sqlite3 import Error

class Database:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "baza.db")
        try:
            self.conn = sqlite3.connect(db_path)
        except Error as e:
            exit(e)

    def insert(self, query, params = ()):
        try:
            self.conn.execute(query, params)
            self.conn.commit()
        except Error as e:
            exit(e)

    def select(self, query, params = ()):
        try:
            cursor = self.conn.execute(query, params)
            return cursor
        except Error as e:
            exit(e)

    def delete(self, query, params = ()):
        try:
            self.conn.execute(query, params)
            self.conn.commit()
        except Error as e:
            exit(e)

    def __del__(self):
        if self.conn:
            self.conn.close()