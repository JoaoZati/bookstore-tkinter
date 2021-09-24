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

window = Tk()

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

#  buttons

b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Seach Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
