from database import Database

class Book:

    def __init__(self, isbn, name, realease_date, publisher):
        self.isbn = isbn
        self.name = name
        self.release_date = realease_date
        self.publisher = publisher
    
    def commit(self):
        database = Database()
        database.insert("INSERT INTO book VALUES (?, ?, ?, ?)", (self.isbn, self.name, self.release_date, self.publisher))
        del database

    @staticmethod
    def delete(isbn):
        if Book.exist(isbn):
            database = Database()
            database.delete("DELETE FROM book WHERE isbn = ?", (isbn, ))
            database.delete("DELETE FROM author_book WHERE isbn = ?", (isbn, ))
            del database

    @staticmethod
    def get_books():
        database = Database()
        cursor = database.select("SELECT * FROM book")
        result = cursor.fetchall()
        del database
        return result

    @staticmethod
    def get_books_for_search_phrase(search_phrase):
        database = Database()
        cursor = database.select('SELECT * FROM book {0}'.format(search_phrase))
        result = cursor.fetchall()
        del database
        return result

    @staticmethod
    def exist(isbn):
        database = Database()
        cursor = database.select("SELECT COUNT(1) FROM book WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()[0]
        del database
        return result