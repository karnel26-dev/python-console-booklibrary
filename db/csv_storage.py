import csv
import os

class CSVStorage:
    def __init__(self, filename):
        file_exist = os.path.isfile(filename)
        self.file = open(filename, "a+", encoding="utf-8")
        fields = ["author", "title", "ISBN", "year", "genre", ]
        writer = csv.DictWriter(self.file, fieldnames=fields)
        if not file_exist:
            writer.writeheader()


    def write_data(self, book: dict):
        writer = csv.DictWriter(self.file, fieldnames=book.keys())
        writer.writerow(book)

    def read_data(self):
        pass