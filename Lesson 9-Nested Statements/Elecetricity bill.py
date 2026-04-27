units=int(input("Enter your units consumed:"))

if units <50:
    amount=units*2.00
    sumcharge=25
elif units<=100:
    amount=130+(units-30)*3.25
    sumcharge=35
elif units<=200:
    amount=130 +162.58 *(units - 100)*5.26
    sumcharge=45
else:
    amount= 130+162.58 + 526 +(units-200)*8.45
    sumcharge=75
total=amount+sumcharge
print("\n" "Electricity bill = %.2f" %total )