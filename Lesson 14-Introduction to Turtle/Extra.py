#pattern
rows=4
for i in range(1,rows,1):
    for j in range(1,i+1,):
        print(j , end=" ")
    print()
    

# Numbers from 1 to 50
num=2
while num<=50:
    print(num,end=" ")
    num+=2

# List and sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))


numbers = [num1, num2, num3, num4, num5]
total_sum = num1 + num2 + num3 + num4 + num5
print("Your list is:", numbers)
print("The total sum is:", total_sum)

# Tables
num=int(input("Enter your number:"))
for i in range(1,11):
    result=num*i
print(f"{num} x {i} = {result}")