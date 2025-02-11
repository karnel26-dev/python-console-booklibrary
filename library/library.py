from . import Book


class Library:
    id_ = 0
    def __init__(self, storage):
        self.books = {}
        self.storage = storage

    def add_book(self, book):
        if isinstance(book, Book):
            Library.id_ += 1
            self.books[Library.id_] = book
            self.storage.write_data(book.to_dict())
            return book
        raise ValueError("Неверный формат книги!")

    def get_book_by_id(self, book_id):
        book = self.books.get(book_id)
        if book:
            return book
        raise ValueError("Такой книги нет")

    def get_book_by_isbn(self, isbn):
        for id_, book in self.books.items():
            if isbn == book.get("isbn"):
                return id_, book

        raise ValueError("Такой книги нет")

    def get_books(self):
        return self.books

    def get_books_by_author(self, author):
        books = {}
        for id_, book in self.books.items():
            if author.lower() in book.author.lower():
                books[id_] = book
        return books

    def get_books_by_title(self, title):
        books = {}
        for id_, book in self.books.items():
            if title.lower() in book.title.lower():
                books[id_] = book
        return books

    def book_delete(self, id_):
        if id_.isdigit():
            if int(id_) in self.books:
                return self.books.pop(int(id_))
        raise ValueError("Неверный или некорректный id")

    @classmethod
    def get_book_count(cls):
        return cls.id_



