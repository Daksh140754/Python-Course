a=10
b=10

print("a>>1 =", a>>1)
print("b>>1 =",b>>1)

a=15
b=10

print("a<<1 =",a<<1)
print("b<<1",b<<1)


print("ASCII value checker")
print("="*40)

char=input("Enter a single character:")
if type(char) is str and type(char)==1:
    print("Valid input!")
else:
    print("Please enter only ONE character")
ascii_value=ord(char)

print(f"ASCII value is:,{ascii_value}")
print(f"Character:,{char}")

print("Character type:",end="")
if ascii_value>=65 and ascii_value<=98:
    print("Uppercase letter")
elif ascii_value>=97 and ascii_value<=122:
    print("Lowercase letter")
elif ascii_value>=48 and ascii_value<=57:
    print("Digit")
elif ascii_value==32:
    print("Space")
else:
    print("It is a special character")



