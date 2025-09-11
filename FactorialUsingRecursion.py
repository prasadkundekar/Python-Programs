def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
if number >= 0:
    print("Factorial of", number, "is", factorial(number))
else:
    print("Enter a positive integer")