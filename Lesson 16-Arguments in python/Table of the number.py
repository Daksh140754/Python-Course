

num=int(input("Enter your number to display its table:"))
if num==0:
    print("Anything multiplied by 0 is 0 ")
elif num==1:
    print("Anything multiplied by 1 is the number itself")
else:
    print(f"The multipliaction table of {num} is:")
for i in range(1,11):
    result=num*i
    print(f"The multipliaction table of the given number is {num} x {i} = {result}")
        

