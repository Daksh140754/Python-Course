try:
    age =int(input("Enter your age:"))
    print("The age entered is:",age)

except ValueError as ex:
    print("Exception:",ex)