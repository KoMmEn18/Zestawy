from database import Database

class AuthorBook:
    @staticmethod
    def add_dependency(id_author, isbn):
        database = Database()
        database.insert("INSERT INTO author_book VALUES (?, ?)", (id_author, isbn))
        del database

    @staticmethod
    def get_authors_for_book(isbn):
        database = Database()
        cursor = database.select("SELECT firstname, lastname FROM author_book INNER JOIN author ON author_book.id_author = author.id WHERE isbn = ?", (isbn, ))
        result = cursor.fetchall()
        del database
        return result

    @staticmethod
    def get_books_for_author(search_phrase):
        database = Database()
        cursor = database.select('  SELECT DISTINCT book.isbn, book.name, book.realease_date, book.publisher \
                                    FROM book LEFT JOIN author_book ON book.isbn = author_book.isbn LEFT JOIN author ON author_book.id_author = author.id \
                                    {0}'.format(search_phrase))
        result = cursor.fetchall()
        del database
        return result
