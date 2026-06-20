import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {user_choice} beats {computer_choice}."
    else:
        result = f"You Lose! {computer_choice} beats {user_choice}."
    
    result_label.config(text=result)
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12)).pack(pady=20)

tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=30)

root.mainloop()