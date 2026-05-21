import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password_length = 12
password = ""
for i in range(password_length):
    password += random.choice(characters)
print("Your password is:", password)