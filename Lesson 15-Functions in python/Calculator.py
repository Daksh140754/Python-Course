def add(P , Q):
    return P+Q
def subtract(P , Q):
    return P-Q
def multiply(P , Q):
    return P*Q
def divide(P , Q):
    return P/Q

print("Please enter a operation:")
print("a,Add")
print("b,Subtract")
print("c,Multiply")
print("d,Divide")

choice=(input("Please enter your choice a/b/c/d:"))

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))

if choice=="a":
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input,please enter the correct input!")