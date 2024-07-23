class Genre:
    def __init__(self, name, description, category):
        self._name = name
        self._description = description
        self._category = category

    def name(self):
        return self._name

    def description(self):
        return self._description

    def category(self):
        return self._category


class Book(Genre):
    def __init__(self, title, author, isbn, publication_date, genre):
        super().__init__(genre.name, genre.description, genre.category)
        self._title = title
        self._author = author
        self._isbn = isbn
        self._publication_date = publication_date
        self._is_borrowed = False

    
    def title(self):
        return self._title


    def author(self):
        return self._author

 
    def isbn(self):
        return self._isbn

  
    def publication_date(self):
        return self._publication_date

 
    def is_borrowed(self):
        return self._is_borrowed

  
    def is_borrowed(self, value):
        self._is_borrowed = value

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Published: {self.publication_date}, Status: {status}, Genre: {self.name}"
