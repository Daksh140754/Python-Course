
num = int(input("Enter the base number: "))
power = int(input("Enter the power (n): "))
result = 1
for i in range(power):
    result = result * num
print(f"{num} raised to the power of {power} is {result}")