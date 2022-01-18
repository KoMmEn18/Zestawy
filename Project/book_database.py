from prettytable import PrettyTable
from author_book import AuthorBook
from author import Author
from book import Book

class BookDatabase:

    def __init__(self):
        print('Welcome in book database! What you wanna do?')

    def run(self):
        self.print_main_menu()
        numberInput = input("Enter number: ")
        if numberInput.isnumeric():
            numberInput = int(numberInput)
            if not (numberInput >= 1 and numberInput <= 5):
                self.print_menu_error_and_go_back()
            if numberInput == 1:
                self.process_book_add()
            elif numberInput == 2:
                self.process_book_delete()
            elif numberInput == 3:
                self.process_book_search()
            elif numberInput == 4:
                self.list_books()
            elif numberInput == 5:
                return
        else:
            self.print_menu_error_and_go_back()

    def process_book_add(self):
        isbn = input("Enter ISBN: ")
        while(Book.exist(isbn)):
            print('Book of given ISBN already exist in database!')
            isbn = input("Enter ISBN: ")
        name = input("Enter book name: ")
        realease_date = input("Enter book release date: ")
        publisher = input("Enter publisher: ")
        book = Book(isbn, name, realease_date, publisher)
        book.commit()

        authors = Author.get_authors()
        if not authors:
            print()
            print("There are no existing authors to choose from. You have to add author first")
            self.add_new_author()
        
        self.process_author_choose(isbn)
        
    def process_author_choose(self, isbn):
        self.print_author_choose_menu()
        numberInput = input("Enter number: ")
        if numberInput.isnumeric():
            numberInput = int(numberInput)
            if not (numberInput >= 1 and numberInput <= 4):
                self.print_author_choose_error_and_go_back(isbn)
            if numberInput == 1:
                self.print_authors()
                authors_id = input("Enter author(s) id (separated by commas if more than one): ")
                authors_id = authors_id.split(',')
                if Book.exist(isbn):
                    for author_id in authors_id:
                        author_id = author_id.strip()
                        if author_id.isnumeric():
                            if Author.exist(author_id):
                                AuthorBook.add_dependency(author_id, isbn)
                    print("Book successfully added!")
                    self.run()
            elif numberInput == 2:
                self.add_new_author()
                self.process_author_choose(isbn)
            elif numberInput == 3:
                self.delete_author()
                self.process_author_choose(isbn)
            elif numberInput == 4:
                self.print_authors()
                self.process_author_choose(isbn)
        else:
            self.print_author_choose_error_and_go_back(isbn)

    def delete_author(self):
        id = input("Enter ID number: ")
        Author.delete(id)
        print('Author of given ID "{0}" (if found in db) was successfully deleted'.format(id))

    def add_new_author(self):
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")
        author = Author(firstname, lastname)
        author.commit()

    def process_book_delete(self):
        isbn = input("Enter ISBN number: ")
        Book.delete(isbn)
        print('Book of given ISBN "{0}" (if found in db) was successfully deleted'.format(isbn))
        self.run()

    def process_book_search(self):
        self.print_search_menu()
        number = input("Enter number: ")
        if number.isnumeric():
            number = int(number)
            if not (number >= 1 and number <= 5):
                self.print_search_error_and_go_back()
            if number == 1:
                self.process_isbn_search()
            elif number == 2:
                self.process_name_search()
            elif number == 3:
                self.process_release_date_search()
            elif number == 4:
                self.process_publisher_search()
            elif number == 5:
                self.process_author_search()
            self.run()
        else:
            self.print_search_error_and_go_back()
   
    def process_isbn_search(self):
        searchPhrase = input("Enter search phrase (ISBN): ")
        books = Book.get_books_for_search_phrase('WHERE isbn LIKE "%{0}%"'.format(searchPhrase))
        result = self.get_author_book_table(books)
        self.print_search_result(result)

    def process_name_search(self):
        searchPhrase = input("Enter search phrase (Name): ")
        books = Book.get_books_for_search_phrase('WHERE name LIKE "%{0}%"'.format(searchPhrase))
        result = self.get_author_book_table(books)
        self.print_search_result(result)

    def process_release_date_search(self):
        searchPhrase = input("Enter search phrase (Release date): ")
        books = Book.get_books_for_search_phrase('WHERE realease_date LIKE "%{0}%"'.format(searchPhrase))
        result = self.get_author_book_table(books)
        self.print_search_result(result)

    def process_publisher_search(self):
        searchPhrase = input("Enter search phrase (Publisher): ")
        books = Book.get_books_for_search_phrase('WHERE publisher LIKE "%{0}%"'.format(searchPhrase))
        result = self.get_author_book_table(books)
        self.print_search_result(result)

    def process_author_search(self):
        searchPhrase = input("Enter search phrase (Author): ")
        books = AuthorBook.get_books_for_author('WHERE author.firstname || " " || author.lastname LIKE "%{0}%"'.format(searchPhrase))
        result = self.get_author_book_table(books)
        self.print_search_result(result)

    def get_author_book_table(self, books):
        result = []
        for row in books:
            ready_row = []
            for record in row:
                ready_row.append(record)
            
            authors = AuthorBook.get_authors_for_book(ready_row[0])
            ready_authors = ""
            for i in range(len(authors)):
                if i + 1 == len(authors):
                    ready_authors += authors[i][0] + " " + authors[i][1]
                else:
                    ready_authors += authors[i][0] + " " + authors[i][1] + ", "

            ready_row.append(ready_authors)
            result.append(ready_row)
        
        return result

    def list_books(self):
        pretty_table = PrettyTable()
        pretty_table.field_names = ["ISBN", "Name", "Release date", "Publisher", "Author(s)"]
        books = Book.get_books()
        if books:
            for row in books:
                ready_row = []
                for record in row:
                    ready_row.append(record)
                
                authors = AuthorBook.get_authors_for_book(ready_row[0])
                ready_authors = ""
                for i in range(len(authors)):
                    if i + 1 == len(authors):
                        ready_authors += authors[i][0] + " " + authors[i][1]
                    else:
                        ready_authors += authors[i][0] + " " + authors[i][1] + ", "

                ready_row.append(ready_authors)
                pretty_table.add_row(ready_row)

            print(pretty_table)
        else:
            print('No books to display')
        self.run()

    def print_authors(self):
        available_authors = Author.get_authors()
        pretty_table = PrettyTable()
        pretty_table.field_names = ["ID", "Firstname", "Lastname"]
        for record in available_authors:
            pretty_table.add_row(record)
        print(pretty_table)

    def print_search_result(self, result):
        if result:
            pretty_table = PrettyTable()
            pretty_table.field_names = ["ISBN", "Name", "Release date", "Publisher", "Author(s)"]
            for record in result:
                pretty_table.add_row(record)
            print(pretty_table)
        else:
            print('No search results for the given phrase')

    def print_search_menu(self):
        print()
        print('Search by: ')
        print('Choose number from 1-5')
        print('============================================')
        print('1. ISBN')
        print('2. Name')
        print('3. Release date')
        print('4. Publisher')
        print('5. Author')
        print('============================================')

    def print_author_choose_menu(self):
        print()
        print('Choose number from 1-4')
        print('============================================')
        print('1. Choose author(s) from list')
        print('2. Add new author')
        print('3. Delete author')
        print('4. List author(s)')
        print('============================================')

    def print_main_menu(self):
        print()
        print('Choose number from 1-5')
        print('============================================')
        print('1. Add book')
        print('2. Delete book')
        print('3. Search for book')
        print('4. List all books')
        print()
        print('5. Exit')
        print('============================================')

    def print_search_error_and_go_back(self):
        print()
        print("This is not a valid number! Try again.")
        self.process_book_search()

    def print_author_choose_error_and_go_back(self, isbn):
        print()
        print("This is not a valid number! Try again.")
        self.process_author_choose(isbn)

    def print_menu_error_and_go_back(self):
        print()
        print("This is not a valid number! Try again.")
        self.run()
