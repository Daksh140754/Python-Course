def shutdown():
    answer=input("Enter your answer (yes/no):").lower()
    if answer=="yes":
        print("Shutting Down")
    elif answer=="no":
        print("Abort Shut Down")
    else:
        print("Sorry")

shutdown()