import tkinter as tk

def check_strength(*args):
    password = entry.get()
    length = len(password)
    
    if length == 0:
        label_res.config(text="", bg="SystemButtonFace")
    elif length <= 5:
        label_res.config(text="Weak", bg="red")
    elif 6 <= length <= 8:
        label_res.config(text="Medium", bg="yellow")
    elif 8 < length <= 12:
        label_res.config(text="Strong", bg="light green")
    else:
        label_res.config(text="Very Strong", bg="dark green")

# 1. & 2. Window Setup
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Widgets
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

# 3. Logic Implementation
password_var = tk.StringVar()
password_var.trace_add("write", check_strength)

entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), show="*")
entry.pack(pady=10)

label_res = tk.Label(root, text="", font=("Arial", 14, "bold"), width=15, height=2)
label_res.pack(pady=20)

root.mainloop()