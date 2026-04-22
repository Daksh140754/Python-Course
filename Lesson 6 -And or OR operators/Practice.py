temp=float(input("Enter Your temperature in fahrenheits:"))
celsius=(temp-32)*5/9
print("The Temperature in celsius is:",celsius)



#length and breadth of a rectangle
l=15
b=15
if (l==b):
    print("It is a square")
else:
    print("It is not a square")


#Program that takes in a number from the user and correctly prints either "that number is between 1 to 100" or "that number is not between 1 to 100"

num=float(input("Enter your number:"))
if num>=1 and num<=100:
    print("That number is between 1 to 100")
else:
    print("That number is not between 1 to 100")

# A program that asks the user to enter a number. You shoudl print out a message to the user,either"That number is divisible by either 3 or 5",or "That number is not divisible by either 3 or 5"

num=int(input("Enter a number:"))
if num% 3 == 0 or num% 5 == 0:
    print("That number is either divisible by either 3 or 5")
else:
    print("That the number is not divisible by either 3 or 5")








  



