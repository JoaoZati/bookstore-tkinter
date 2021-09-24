import sqlite3


def connect():
    conection = sqlite3.connect('books.db')
    cursor = conection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book "
                   "(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    return conection, cursor


def close(conection):
    conection.commit()
    conection.close()


def add_entry(title: str, author: str, year: int, isbn: int):
    conection, cursor = connect()
    cursor.execute(f"INSERT INTO book VALUES (NULL, '{title}', '{author}', {year}, {isbn})")
    close(conection)


def view_all():
    conection, cursor = connect()
    cursor.execute(f"SELECT * FROM book")
    rows = cursor.fetchall()
    close(conection)
    return rows


def search_entry(title="", author="", year="", isbn=""):
    conection, cursor = connect()
    cursor.execute(f"SELECT * FROM book WHERE title='{title}' OR author='{author}' OR year=? OR isbn=?", (year, isbn))
    rows = cursor.fetchall()
    close(conection)
    return rows


def delete_select(id: int):
    conection, cursor = connect()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    rows = cursor.fetchall()
    close(conection)
    return rows


def update_select(id: int, title, author, year, isbn):
    conection, cursor = connect()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, id))
    rows = cursor.fetchall()
    close(conection)
    return rows


update_select(1, "The moon", "John Tablet", 1918, 913123124)
print(view_all())
