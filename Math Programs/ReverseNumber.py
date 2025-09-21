def reverse_number(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    reversed_num = 0

    # Handle negative numbers
    sign = -1 if n < 0 else 1
    n = abs(n)

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num * sign

number = 12345
reversed_result = reverse_number(number)
print(f"The reversed number is: {reversed_result}")

number2 = -9876
reversed_result2 = reverse_number(number2)
print(f"The reversed number is: {reversed_result2}")