from tkinter import *
from tkinter import messagebox
import backend

window = Tk()

window.wm_title("BookStore")

def get_selected_row(event):
    if len(l1.curselection()) != 0:
        index = l1.curselection()[0]
        global selected_tuple
        selected_tuple = l1.get(first = index)
        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[2])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[3])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
    '''
    another method
    try:
        index = l1.curselection()[0]
        global selected_tuple
        selected_tuple = l1.get(first = index)
        t1.delete(0, END)
        t1.insert(END, selected_tuple[1])
        t2.delete(0, END)
        t2.insert(END, selected_tuple[2])
        t3.delete(0, END)
        t3.insert(END, selected_tuple[3])
        t4.delete(0, END)
        t4.insert(END, selected_tuple[4])
    except: IndexError:
        pass
    '''

def view_all():
    content = backend.view()
    l1.delete(0, END)
    for book in content:
        l1.insert(END, book)

def add_entry():
    if title.get() == "" and author.get() == "" and year.get() == "" and isbn.get() == "":
        messagebox.showerror("Error", "You pressed the Add button while there's nothing to add")
    else:
        backend.insert(title.get(), author.get(), year.get(), isbn.get())
        l1.delete(0, END)
        view_all()

def search_entry():
    result = backend.search(title.get(), author.get(), year.get(), isbn.get())
    l1.delete(0, END)
    for book in result:
        l1.insert(END, book)

def update_selected():
    backend.update(selected_tuple[0], title.get(), author.get(), year.get(), isbn.get())
    view_all()

def delete_selected():
    backend.delete(selected_tuple[0])
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    view_all()

def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)      
    t4.delete(0, END)  
    l1.delete(0, END)  

#Messages
m1 = Message(window, text = "Title")
m1.grid(row = 0, column = 0)
m2 = Message(window, text = "Author")
m2.grid(row = 0, column = 2)
m3 = Message(window, text = "Year")
m3.grid(row = 1, column =0)
m4 = Message(window, text = "ISBN")
m4.grid(row = 1, column =2)

#Entries
title = StringVar()
t1 = Entry(window, textvariable = title)
t1.grid(row = 0, column =1)
author = StringVar()
t2 = Entry(window, textvariable = author)
t2.grid(row = 0, column = 3)
year = StringVar()
t3 = Entry(window, textvariable = year)
t3.grid(row =1, column =1)
isbn = StringVar()
t4 = Entry(window, textvariable = isbn)
t4.grid(row = 1, column =3)

#Listbox
l1 = Listbox(window, height = 6, width = 35)
l1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#Buttons
b1 = Button(window, text = "View All", width = 12, command = view_all)
b1.grid(row = 2, column = 3)
b2 = Button(window, text = "Search Entry", width = 12, command = search_entry)
b2.grid(row = 3, column = 3)
b3 = Button(window, text = "Add Entry", width = 12, command = add_entry)
b3.grid(row = 4, column = 3)
b4 = Button(window, text = "Update Selected", width = 12, command = update_selected)
b4.grid(row = 5, column = 3)
b5 = Button(window, text = "Delete Selected", width = 12, command = delete_selected)
b5.grid(row = 6, column =3)
b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 8, column = 3)
b7  =Button(window, text = "Clear", width = 12, command = clear)
b7.grid(row = 7, column = 3)

#scrollbar
sc1 = Scrollbar(window)
sc1.grid(row = 2, column = 2, rowspan = 6)

#configure the scrollbar with the list
l1.configure(yscrollcommand = sc1.set)
sc1.configure(command = l1.yview)

#bind the list
l1.bind('<<ListboxSelect>>', get_selected_row)

window.mainloop()