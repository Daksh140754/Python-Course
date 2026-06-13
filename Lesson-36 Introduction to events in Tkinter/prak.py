import tkinter as tk

def convert():
  
    user_input = entry_box.get()
    inches = float(user_input)
    centimeters = inches * 2.54
    final_text = f"{inches} inches is equal to {centimeters:} cm"
    result_label.config(text=final_text)
window = tk.Tk()
window.title("Inches to CM Converter")
window.geometry("400x250")  
instruction_label = tk.Label(window, text="Please enter the length in inches:")

instruction_label.pack(pady=10) 
entry_box = tk.Entry(window)
entry_box.pack(pady=10)
convert_button = tk.Button(window, text="Convert Now", command=convert)
convert_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
window.mainloop()




