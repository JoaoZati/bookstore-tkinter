import sqlite3


class Database:
    def __init__(self, db):
        self.conection = sqlite3.connect(db)
        self.cursor = self.conection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS 'book' "
                            "(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conection.commit()
        self.conection.close()

    def connect(self):
        self.conection = sqlite3.connect('books.db')
        self.cursor = self.conection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS book "
                            "(id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")

    def close(self):
        self.conection.commit()
        self.conection.close()

    def insert_data(self, title: str, author: str, year: int, isbn: int):
        self.connect()
        self.cursor.execute(f"INSERT INTO book VALUES (NULL, '{title}', '{author}', {year}, {isbn})")
        self.close()

    def view_data(self):
        self.connect()
        self.cursor.execute(f"SELECT * FROM book")
        rows = self.cursor.fetchall()
        self.close()
        return rows

    def search_data(self, title="", author="", year="", isbn=""):
        self.connect()
        self.cursor.execute(f"SELECT * FROM book WHERE title='{title}' OR author='{author}' OR year=? OR isbn=?",
                       (year, isbn))
        rows = self.cursor.fetchall()
        self.close()
        return rows

    def delete_data(self, id: int):
        self.connect()
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        rows = self.cursor.fetchall()
        self.close()
        return rows

    def update_data(self, id: int, title, author, year, isbn):
        self.connect()
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                       (title, author, year, isbn, id))
        rows = self.cursor.fetchall()
        self.close()
        return rows

    def last_data(self):
        self.connect()
        self.cursor.execute("SELECT * FROM book ORDER BY ID DESC LIMIT 1")
        row = self.cursor.fetchall()
        self.close()
        return row

    def search_data_by_id(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = self.cursor.fetchall()
        self.close()
        return rows


if __name__ == '__main__':
    data_books = Database()
    print(data_books.view_data())
