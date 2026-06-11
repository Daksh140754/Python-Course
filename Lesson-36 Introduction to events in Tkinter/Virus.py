from tkinter import *

from tkinter import messagebox

root = Tk()
root.title("Virus Detected")
root.geometry('960x360')

def msg():
    messagebox.showwarning("Alert" , "Stop Virus Found!!")

button = Button(root , text="Scan For Virus" ,command=msg)

button.place(x=40 , y=80)
root.mainloop()