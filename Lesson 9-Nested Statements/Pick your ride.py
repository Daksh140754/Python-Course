print("Pick your ride:")
print("1 , Bike")
print("2 , Car")
choice=int(input("Enter Your Choice:"))
if choice==1:
    print("You have chosen bike:")
    print("1 , scooter")
    print("2 , scooty")
    choice2=int(input("Enter your type:"))
    if choice2==1:
         print("You have chosen scooter")
    else:
        print("You have chosen scooty")

elif choice==2:
    print("You have chosen Car:")
    print("1 , XUV")
    print("2 , Sedan")
    choice2=int(input("Enter your type:"))
    if choice2==1:
         print("You have chosen XUV")
    else:
        print("You have chosen Sedan")
else:
    print("Invalid input")



  