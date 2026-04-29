

num = int(input("Enter a number: "))
if num < 0:
    n = -num 
else:
    n = num
count = 0
if n == 0:
    count = 1
else: 
    while n > 0:
        n = n // 10
        count = count + 1
print(f"The number of digits in {num} is {count}")