from frontend_oo import Window
from backend_oo import Database

books = Database('books.db')
window = Window(books)
window.main_loop()
