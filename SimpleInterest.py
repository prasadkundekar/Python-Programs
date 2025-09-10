principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (%): "))
time = float(input("Enter the time (years): "))

simple_interest = (principal * rate * time) / 100

print(f"Simple Interest: ${simple_interest:.2f}")