num = int(input("Enter your number: "))
original_num = num
binary_result = 0
place_value = 1

if num < 0:
    print("Please enter a positive number.")
elif num == 0:
    print("The binary form of the entered number is: 0")
else:
   
    while num > 0:
        remainder = num % 2        
        binary_result = binary_result + (remainder * place_value)
        place_value = place_value * 10
        num = num // 2
    
    print(f"The binary form of {original_num} is: {binary_result}")