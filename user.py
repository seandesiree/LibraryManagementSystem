class User:
    def __init__(self, name, library_id):
        self._name = name
        self._library_id = library_id
        self._borrowed_books = []

  
    def name(self):
        return self._name


    def library_id(self):
        return self._library_id


    def borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book):
        if book not in self._borrowed_books:
            self._borrowed_books.append(book)

    def return_book(self, book):
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self._borrowed_books])
        return f"Name: {self.name}, Library ID: {self.library_id}, Borrowed Books: {borrowed_titles}"
