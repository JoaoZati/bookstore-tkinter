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
import backend


def get_selected_row(event):
    global selected_tuple
    global index
    index = listbox.curselection()[0]  # Retorna o id (da para fazer global index)
    selected_tuple = listbox.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def delete_command():
    backend.delete_data(selected_tuple[0])
    listbox.delete(index)


def update_command():
    backend.update_data(selected_tuple[0],
                        title_entry.get(),
                        author_entry.get(),
                        year_entry.get(),
                        isbn_entry.get())
    row = backend.search_data_by_id(selected_tuple[0])[0]
    listbox.delete(index)
    print(row)
    listbox.insert(index, row)


def view_command():
    listbox.delete(0, END)
    for row in backend.view_data():
        listbox.insert(END, row)


def seach_command():
    listbox.delete(0, END)
    for row in backend.search_data(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()):
        listbox.insert(END, row)


def add_command():
    backend.insert_data(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    row = backend.last_data()[0]
    listbox.insert(END, row)


window = Tk()

window.wm_title("BookStore")
#  Label and entrys (user)

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_entry = StringVar()
e1 = Entry(window, textvariable=title_entry)
e1.grid(row=0, column=1)

author_entry = StringVar()
e2 = Entry(window, textvariable=author_entry)
e2.grid(row=0, column=3)

year_entry = StringVar()
e3 = Entry(window, textvariable=year_entry)
e3.grid(row=1, column=1)

isbn_entry = StringVar()
e4 = Entry(window, textvariable=isbn_entry)
e4.grid(row=1, column=3)

#  Scrowbar and listbox

listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

#  buttons

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Seach Entry", width=12, command=seach_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
