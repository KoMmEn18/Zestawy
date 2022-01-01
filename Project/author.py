from database import Database

class Author:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def commit(self):
        database = Database()
        database.insert("INSERT INTO author (firstname, lastname) VALUES (?, ?)", (self.firstname, self.lastname))
        del database

    @staticmethod
    def delete(id):
        if Author.exist(id):
            database = Database()
            database.delete("DELETE FROM author WHERE id = ?", (id, ))
            database.delete("DELETE FROM author_book WHERE id_author = ?", (id, ))
            del database

    @staticmethod
    def get_authors():
        database = Database()
        cursor = database.select("SELECT * FROM author")
        result = cursor.fetchall()
        del database
        return result

    @staticmethod
    def exist(id):
        database = Database()
        cursor = database.select("SELECT COUNT(1) FROM author WHERE id = ?", (id,))
        result = cursor.fetchone()[0]
        del database
        return result