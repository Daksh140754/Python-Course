import tkinter as tk
from datetime import date


def calculate():
    user_day = entry_day.get()
    user_month = entry_month.get()
    user_year = entry_year.get()

    day_number = int(user_day)
    month_number = int(user_month)
    year_number = int(user_year)

    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    calculated_age = current_year - year_number

    if current_month < month_number:
        calculated_age = calculated_age - 1
    elif current_month == month_number:
        if current_day < day_number:
            calculated_age = calculated_age - 1

    output_message = "Your present age is: " + str(calculated_age) + " years"

    result_label.config(text=output_message)


window = tk.Tk()
window.title("Age Calculator Application")
window.geometry("400x350")

main_title = tk.Label(window, text="Age Calculator")
main_title.pack(pady=10)

day_title = tk.Label(window, text="Enter Birth Day (1-31):")
day_title.pack(pady=2)

entry_day = tk.Entry(window)
entry_day.pack(pady=5)

month_title = tk.Label(window, text="Enter Birth Month (1-12):")
month_title.pack(pady=2)

entry_month = tk.Entry(window)
entry_month.pack(pady=5)

year_title = tk.Label(window, text="Enter Birth Year (e.g. 2010):")
year_title.pack(pady=2)

entry_year = tk.Entry(window)
entry_year.pack(pady=5)

submit_button = tk.Button(window, text="Calculate Age Now", command=calculate)
submit_button.pack(pady=15)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()