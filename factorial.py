def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from the user
n = int(input("Enter a number: "))

result = calculate_factorial(n)
print(f"The factorial of {n} is {result}")