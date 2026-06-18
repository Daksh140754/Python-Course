import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p = float(entry_p.get())
        t = float(entry_t.get())
        r = float(entry_r.get())
        
        si = (p * t * r) / 100
        ci = p * (pow((1 + r / 100), t)) - p
        
        label_si_val.config(text=f"{si:.2f}")
        label_ci_val.config(text=f"{ci:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# 1. & 2. Window setup
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# 3. & 4. Using labels and entry widgets side by side (grid manager)
tk.Label(root, text="Principle:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
entry_p = tk.Entry(root)
entry_p.grid(row=0, column=1)

tk.Label(root, text="Time (years):", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
entry_t = tk.Entry(root)
entry_t.grid(row=1, column=1)

tk.Label(root, text="Rate of Interest (%):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
entry_r = tk.Entry(root)
entry_r.grid(row=2, column=1)

btn_calc = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white")
btn_calc.grid(row=3, column=0, columnspan=2, pady=20)

# 5. Display the values
tk.Label(root, text="Simple Interest:", font=("Arial", 10, "bold")).grid(row=4, column=0)
label_si_val = tk.Label(root, text="0.00", fg="blue")
label_si_val.grid(row=4, column=1)

tk.Label(root, text="Compound Interest:", font=("Arial", 10, "bold")).grid(row=5, column=0)
label_ci_val = tk.Label(root, text="0.00", fg="blue")
label_ci_val.grid(row=5, column=1)

root.mainloop()