valid=False
while not valid:
    try:
        a=int(input("Enter a number:"))
        while a%2==0:
            print("Bye")
        valid=True
    except ValueError:
        print("Invalid input !")