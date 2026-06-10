from tkinter import *

root = Tk()
root.title("Login App")
root.geometry('600x500')

frame = Frame(master=root , height=500 , width=500 , bg='grey' )

a1 = Label(frame , text="Full name" , bg='white' , fg='black', width=12)
a2 = Label(frame , text="Email Id" , bg='white' , fg='black', width=12)
a3 = Label(frame , text="Password" , bg='white' , fg='black', width=12)

name_Entry = Entry(frame)
email_entry = Entry(frame)
password_entry= Entry(frame , show="*")

def display():
    name = name_Entry.get()
    greet = "Hey"+name
    message = "\nCongratulations For Your New Account"
    textbox.insert(END , greet)
    textbox.insert(END , message)

textbox = Text(bg='white' ,fg = 'blue')
btn = Button(text= "Create Account" , command=display , bg="red")

frame.place(x=20 , y=0)
a1.place(x=20 , y=20)
name_Entry.place(x=150,  y=20)
a2.place(x=20,  y=80)
email_entry.place(x=150,  y=80)
a3.place(x=20,  y=140)
password_entry.place(x=150,  y=140)
btn.place(x=130,  y=210)
textbox.place(y=250)

root.mainloop()