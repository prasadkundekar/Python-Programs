def find_gcd(a, b):
    while (b):
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (abs(a * b)) // find_gcd(a, b)
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd_result = find_gcd(num1, num2)
    lcm_result = find_lcm(num1, num2)

    print(f"\nThe GCD of {num1} and {num2} is: {gcd_result}")
    print(f"The LCM of {num1} and {num2} is: {lcm_result}")

except ValueError:
    print("Invalid input. Please enter integers.")