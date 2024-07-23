from book import Book
from user import User
from author import Author
from genre import Genre


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book, user):
        if not book.is_borrowed:
            book.is_borrowed = True
            user.borrow_book(book)
        else:
            print(f"The book '{book.title}' is already borrowed.")

    def return_book(self, book, user):
        if book.is_borrowed:
            book.is_borrowed = False
            user.return_book(book)
        else:
            print(f"The book '{book.title}' was not borrowed.")

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_books(self):
        for book in self.books:
            print(book)

    def add_user(self, user):
        self.users.append(user)

    def view_user_details(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return user
        return None

    def display_users(self):
        for user in self.users:
            print(user)

    def add_author(self, author):
        self.authors.append(author)

    def view_author_details(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None

    def display_authors(self):
        for author in self.authors:
            print(author)

    def add_genre(self, genre):
        self.genres.append(genre)

    def view_genre_details(self, name):
        for genre in self.genres:
            if genre.name == name:
                return genre
        return None

    def display_genres(self):
        for genre in self.genres:
            print(genre)
