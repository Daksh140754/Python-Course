
limit = int(input("Enter the upper limit for your range: "))
even_squares = []
odd_squares = []

for i in range(1, limit + 1):
    square = i ** 2 
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print(f"Even Squares: {even_squares}")
print(f"Odd Squares:  {odd_squares}")