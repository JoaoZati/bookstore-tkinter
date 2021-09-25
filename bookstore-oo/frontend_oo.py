"""
A program that stores this book information:
Title, Author, Year, ISBN

User can:
View all records
Seach a entry
Add a entry
Update a entry
Delete
Close
"""

from tkinter import *
from backend_oo import Database


class Window:
    type = 'window'

    def __init__(self, database: object, window_tk=False):
        self.database = database
        self.window = Tk()
        if window_tk:
            self.window = window_tk

        self.window.wm_title('Bookstore')

        self.l1 = Label(self.window, text='Title')
        self.l1.grid(row=0, column=0)

        self.l2 = Label(self.window, text='Author')
        self.l2.grid(row=0, column=2)

        self.l3 = Label(self.window, text='Year')
        self.l3.grid(row=1, column=0)

        self.l4 = Label(self.window, text='ISBN')
        self.l4.grid(row=1, column=2)

        self.title_entry = StringVar()
        self.e1 = Entry(self.window, textvariable=self.title_entry)
        self.e1.grid(row=0, column=1)

        self.author_entry = StringVar()
        self.e2 = Entry(self.window, textvariable=self.author_entry)
        self.e2.grid(row=0, column=3)

        self.year_entry = StringVar()
        self.e3 = Entry(self.window, textvariable=self.year_entry)
        self.e3.grid(row=1, column=1)

        self.isbn_entry = StringVar()
        self.e4 = Entry(self.window, textvariable=self.isbn_entry)
        self.e4.grid(row=1, column=3)

        self.listbox = Listbox(self.window, height=6, width=35)
        self.listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=2, rowspan=6)

        self.listbox.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.listbox.yview)

        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        self.b1 = Button(self.window, text="View All", width=12, command=self.view_command)
        self.b1.grid(row=2, column=3)

        self.b2 = Button(self.window, text="Seach Entry", width=12, command=self.search_command)
        self.b2.grid(row=3, column=3)

        self.b3 = Button(self.window, text="Add Entry", width=12, command=self.add_command)
        self.b3.grid(row=4, column=3)

        self.b4 = Button(self.window, text="Update", width=12, command=self.update_command)
        self.b4.grid(row=5, column=3)

        self.b5 = Button(self.window, text="Delete", width=12, command=self.delete_command)
        self.b5.grid(row=6, column=3)

        self.b6 = Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        global selected_tuple
        global index
        try:
            index = self.listbox.curselection()[0]  # Retorna o id (da para fazer global index)
            selected_tuple = self.listbox.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def delete_command(self):
        self.database.delete_data(selected_tuple[0])
        self.listbox.delete(index)

    def update_command(self):
        self.database.update_data(selected_tuple[0],
                                  self.title_entry.get(),
                                  self.author_entry.get(),
                                  self.year_entry.get(),
                                  self.isbn_entry.get()
                                  )
        row = self.database.search_data_by_id(selected_tuple[0])[0]
        self.listbox.delete(index)
        print(row)
        self.listbox.insert(index, row)

    def view_command(self):
        self.listbox.delete(0, END)
        for row in self.database.view_data():
            self.listbox.insert(END, row)

    def search_command(self):
        self.listbox.delete(0, END)
        for row in self.database.search_data(self.title_entry.get(),
                                             self.author_entry.get(),
                                             self.year_entry.get(),
                                             self.isbn_entry.get()
                                             ):
            self.listbox.insert(END, row)

    def add_command(self):
        self.database.insert_data(
            self.title_entry.get(),
            self.author_entry.get(),
            self.year_entry.get(),
            self.isbn_entry.get()
        )
        row = self.database.last_data()[0]
        self.listbox.insert(END, row)

    def main_loop(self):
        self.window.mainloop()


if __name__ == '__main__':
    books = Database('books.db')
    window = Window(books)
    window.main_loop()
