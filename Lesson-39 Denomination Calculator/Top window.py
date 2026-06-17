from tkinter import *

root=Tk()
root.title("Main")
root.geometry('960x500')

def topwin():
    top = Toplevel()
    top.title("Top window")
    top.geometry('1000x600')

    l2 = Label(top , text="This is a Top Level Window")
    l2.pack()


    top.mainloop()


l = Label(root , text="This is a root window")
btn = Button(text="Click here to open another window" , command=topwin)

l.pack()
btn.pack()

root.mainloop()



