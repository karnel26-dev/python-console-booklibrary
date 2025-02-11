from . import Book


class Library:
    def __init__(self, storage):
        self.books = {}
        self.storage = storage
        self.last_id = None

    def _get_last_id_book(self):
        last_id = self.storage.get_last_id()
        return last_id

    def increment_book_id(self):
        self.last_id = int(self._get_last_id_book())
        self.last_id += 1
        self.storage.increment_last_id()

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.increment_book_id()
            book.id = str(self.last_id)
            self.storage.write_data(book.to_dict())
            return book
        raise ValueError("Неверный формат книги!")

    def get_book_by_id(self, book_id: str):
        book = self.books.get(book_id)
        if book:
            return book
        raise ValueError("Такой книги нет")

    def get_book_by_isbn(self, isbn: str):
        for id_, book in self.books.items():
            if isbn == book.get("isbn"):
                return id_, book
        raise ValueError("Такой книги нет")

    def get_books(self):
        books = self.storage.read_data()
        books_obj = []
        for book in books:
            books_obj.append(Book.from_dict(book))
        return books_obj

    def get_books_by_author(self, author: str):
        books = {}
        for id_, book in self.books.items():
            if author.lower() in book.author.lower():
                books[id_] = book
        return books

    def get_books_by_title(self, title: str):
        books = {}
        for id_, book in self.books.items():
            if title.lower() in book.title.lower():
                books[id_] = book
        return books

    def book_delete(self, id_: str):
        if id_.isdigit():
            if int(id_) in self.books:
                return self.books.pop(int(id_))
        raise ValueError("Неверный или некорректный id")

    def get_book_count(self):
        pass



