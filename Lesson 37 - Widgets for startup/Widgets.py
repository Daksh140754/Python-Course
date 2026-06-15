from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with widgets")
root.geometry('400x400')

e = Label(text = "Hey there" , fg = 'white' , bg = 'grey' , height = 1 , width= 100)


b = Label(text = "full name" , bg = 'red')
b_entry = Entry()

def display():

    b = b_entry.get()

    global Message

    message = ("Welcome to the application \nand todays date is:")
    greet = "Hello"+b+ "\n"

    text_box.insert(END , greet)
    text_box.insert(END , message)
    text_box.insert(END , date.today())



text_box = Text(height = 9)

btn = Button(text = 'Begin' , command=display , height= 1 , bg='black' , fg = 'white')

e.pack()
b.pack()
b_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()