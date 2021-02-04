book_page = {
    "Coraline": 224,
    "Labirinto do fauno": 320,
    "A Coragem de ser imperfeito": 226,
    "Me poupe": 176,
    "Duna": 680
}

print(book_page["Coraline"])
print(book_page.get("Harry Potter", -1))
print(book_page.get("Me poupe", -1))
print(book_page.get("Duna", -1))

for book in book_page:
    print(book)

book_page["A Torre de Nero"] = 336

for book in book_page:
    print(book)

for book in book_page.keys():
    print(book)

for book in book_page.values():
    print(book)

for book in book_page.keys():
    value = book_page[book]
    print(book)

for book in book_page.items():
    print(book)

for book, pages in book_page.items():
    print(book, "tem", pages, "páginas")

del book_page["Coraline"]

print("\nCoraline deletado\n")

for book, page in book_page.items():
    print(book, "tem", page, "páginas")

