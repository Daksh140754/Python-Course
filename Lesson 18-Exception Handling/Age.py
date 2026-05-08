try:
    age=int(input("Enter your age:"))
    
    if age<=0:
        print("The age cannot be negative or 0")
    else:
        if age%2==0:
            print("The age entered is a even number")
        else:
            print("The age entered is an odd number")

except ValueError as ex:
    print("Invalid input, please enter a whole number not a special character!!!!!",ex)




