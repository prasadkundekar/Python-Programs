P = int(input("Enter starting principle please: "))
n = int(input("Enter number of compounding periods per year: "))
r = float(input("Enter annual interest rate: "))
y = int(input("Enter the amount of years: "))

FV = P * (((1 + ((r / 100.0) / n)) ** (n * y)))

print("The final amount after", y, "years is", FV)
