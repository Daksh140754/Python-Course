class Employee:

    def __init__(self):
        print("Constructor created")


    def __del__(self):
        print("Destructor created")


def create_obj():
    print("Making object.....")
    obj = Employee
    print("Onject created")
    return obj
    

print("Calling the object function.....")
obj = create_obj()
print("Program Ends....")