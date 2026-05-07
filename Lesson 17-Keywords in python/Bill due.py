total=float(input("Enter the total amount:"))
amtpaid=float(input("Enter the amount paid:"))
due=total-amtpaid
if total>amtpaid:
    due=total-amtpaid
    print(f"The amount due is${due}")
else:
    due=amtpaid-total
    print(f"The amount due is ${due}")