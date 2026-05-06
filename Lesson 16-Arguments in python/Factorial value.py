def factorial(x):
    """This is a recursive function"""

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print("The factorial of 0:",factorial(0))
print("The factorial of 2:",factorial(2))
print("The factorial of 5:",factorial(5))
print("The factorial of 10:",factorial(10))
print("The factorial of 3:",factorial(3))
print(factorial.__doc__)