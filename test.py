books = [
    {"isbn": "2"}, #0
    {"isbn": "3"}, #1
    {"isbn": "4"}  #2
]

for i, book in enumerate(books):
    if book["isbn"] == "2":
        books.pop(i)

print(books)