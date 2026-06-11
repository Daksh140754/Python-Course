from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry('960x360')

def handle_keypressed(event):
    """Print the character associated with the key pressed"""
    print(event.char)


root.bind("<Key>" ,handle_keypressed)


def handle_click(event):
    print("\nThe button was clicked!")


button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>" , handle_click)

root.mainloop()