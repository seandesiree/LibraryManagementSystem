import re
from library import Library
from book import Book
from user import User
from author import Author
from genre import Genre


class LibraryCLI:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Return to Main Menu")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_new_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.library.display_books()
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")

    def add_new_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        isbn = input("Enter the ISBN: ")
        publication_date = input("Enter the publication date (YYYY-MM-DD): ")
        genre_name = input("Enter the genre name: ")
        genre_description = input("Enter the genre description: ")
        genre_category = input("Enter the genre category: ")
        genre = Genre(genre_name, genre_description, genre_category)
        book = Book(title, author, isbn, publication_date, genre)
        self.library.add_book(book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        isbn = input("Enter the ISBN of the book to borrow: ")
        library_id = input("Enter your library ID: ")
        book = self.library.search_book(isbn)
        user = self.library.view_user_details(library_id)
        if book and user:
            self.library.borrow_book(book, user)
            print(f"Book '{book.title}' borrowed by '{user.name}'.")
        else:
            print("Invalid book ISBN or library ID.")

    def return_book(self):
        isbn = input("Enter the ISBN of the book to return: ")
        library_id = input("Enter your library ID: ")
        book = self.library.search_book(isbn)
        user = self.library.view_user_details(library_id)
        if book and user:
            self.library.return_book(book, user)
            print(f"Book '{book.title}' returned by '{user.name}'.")
        else:
            print("Invalid book ISBN or library ID.")

    def search_book(self):
        isbn = input("Enter the ISBN of the book to search: ")
        book = self.library.search_book(isbn)
        if book:
            print(book)
        else:
            print("Book not found.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Return to Main Menu")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_new_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.library.display_users()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def add_new_user(self):
        name = input("Enter the user's name: ")
        library_id = input("Enter the user's library ID: ")
        user = User(name, library_id)
        self.library.add_user(user)
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter the library ID of the user to view: ")
        user = self.library.view_user_details(library_id)
        if user:
            print(user)
        else:
            print("User not found.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Return to Main Menu")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_new_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.library.display_authors()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def add_new_author(self):
        name = input("Enter the author's name: ")
        biography = input("Enter the author's biography: ")
        author = Author(name, biography)
        self.library.add_author(author)
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter the name of the author to view: ")
        author = self.library.view_author_details(name)
        if author:
            print(author)
        else:
            print("Author not found.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Return to Main Menu")

            choice = input("Choose an option: ")
            if choice == '1':
                self.add_new_genre()
            elif choice == '2':
                self.view_genre_details()
            elif choice == '3':
                self.library.display_genres()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

    def add_new_genre(self):
        name = input("Enter the genre name: ")
        description = input("Enter the genre description: ")
        category = input("Enter the genre category: ")
        genre = Genre(name, description, category)
        self.library.add_genre(genre)
        print(f"Genre '{name}' added successfully.")

    def view_genre_details(self):
        name = input("Enter the name of the genre to view: ")
        genre = self.library.view_genre_details(name)
        if genre:
            print(genre)
        else:
            print("Genre not found.")
