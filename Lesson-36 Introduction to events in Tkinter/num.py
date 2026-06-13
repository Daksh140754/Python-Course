import tkinter as tk


def multiply_numbers():
    first_input = entry_number1.get()
    second_input = entry_number2.get()

    number1 = float(first_input)
    number2 = float(second_input)

    product = number1 * number2

    final_answer = "The product is: " + str(product)

    result_label.config(text=final_answer)


window = tk.Tk()
window.title("Multiplication Application")
window.geometry("400x300")

main_heading = tk.Label(window, text="Number Multiplier")
main_heading.pack(pady=10)

label1 = tk.Label(window, text="Enter First Number:")
label1.pack(pady=2)

entry_number1 = tk.Entry(window)
entry_number1.pack(pady=5)

label2 = tk.Label(window, text="Enter Second Number:")
label2.pack(pady=2)

entry_number2 = tk.Entry(window)
entry_number2.pack(pady=5)

multiply_button = tk.Button(window, text="Multiply", command=multiply_numbers)
multiply_button.pack(pady=15)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()