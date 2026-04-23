print("Enter your grade in 5 subjects:")
math=int(input("Enter your marks in maths:"))
engl=int(input("Enter your marks in english:"))
hind=int(input("Enter your marks in hindi:"))
scie=int(input("Enter your marks in science:"))
soci=int(input("Enter your marks in social:"))

sum=math+engl+hind+scie+soci

avg=sum/5

if avg >=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<=91:
    print("Your grade is A2")
elif avg>=71 and avg<=81:
    print("Your grade is B1")
elif avg>=61 and avg<=71:
    print("Your grade is B2")
else:
    print("The value given is invalid")
