try:
    num1 , num2=eval(input("Enter two numbers,separated by a comma: "))
    result=num1/num2
    print("Result is",result)

except ZeroDivisionError:
    print("Division by zero is not defined")
except SyntaxError:
    print("Comma is missing, enter numbers separated by a comma! ")
except:
    print("Invalid input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what !!!")