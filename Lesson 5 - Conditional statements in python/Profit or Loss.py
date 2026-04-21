actual_price=float(input("Enter your actual item price:"))
sale_price=float(input("Enter the sale price:"))
amount=sale_price-actual_price
if sale_price > actual_price:
    print("It is a profit",amount)
else:
    print("It is a loss",amount)




