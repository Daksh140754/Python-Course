
user_input = int(input("Enter a number: "))
full_list = list(range(1, user_input))
odd_numbers = [x for x in full_list if x % 2 != 0]
print("All numbers:", full_list)
print("Odd numbers under your input:", odd_numbers)
fruits = ["apple", "banana", "cherry", "mango", "strawberry"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Original list:", fruits)
print("Updated list:", capitalized_fruits)