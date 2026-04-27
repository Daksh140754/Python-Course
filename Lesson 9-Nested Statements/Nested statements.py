medical_cause=input("Enter your medical cause if any (Y/N):").strip().upper()
if medical_cause == "Y":
    print("You are eligible to write the exam")
else:
    attendance=int(input("Enter your attendance:"))

    if attendance>=75:
     print("You are allowed to write the exam")
    else:
     print("You are not allowed to write the exam")