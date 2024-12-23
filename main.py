# Создаем список книг
books = [
    {"title": "Война и мир", "author": "Лев Толстой", "year": 1869},
    {"title": "Дом в котором", "author": "Мариам Петросян", "year": 2009},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967},
    {"title": "Анна Каренина", "author": "Лев Толстой", "year": 1877}
]

# Цикл для вывода информации о каждой книге
for i, book in enumerate(books, start=1):
    print(f"---------------------- Книга {i} -----------------------")
    print(f"Название: {book['title']}, Автор: {book['author']},")
    print(f"-------------------------{book['year']}-------------------------")
    print()

# Пример вывода:
# ---------------------- Книга 1 -----------------------
# Название: Война и мир, Автор: Лев Толстой,
# -------------------------1869-------------------------
#
# ---------------------- Книга 2 -----------------------
# Название: Дом в котором, Автор: Мариам Петросян,
# -------------------------2009-------------------------
#
# и т.д.
