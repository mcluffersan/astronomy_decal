class Book:
    def __init__(self,title,isbn, author, available_copies):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.available_copies = available_copies

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

class Libary:
    def __init__(self, books):
        self.books = books
    
    def add_book(self, book):
        self.books = self.books.append(book)

    def serach_books_by_author(self, author_name):
        same_author = []
        i = 0
        while i<len(self.books):
            if self.books[i].author == author_name:
                same_author = same_author.append(self.books[i])
            i += 1
        return same_author

    def search_available_books(self, title_keyword):
        available_books = []
        for book in self.books:
