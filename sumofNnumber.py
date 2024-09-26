def sum_of_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter the value of n: "))

result = sum_of_n_numbers(n)
print(f"The sum of the first {n} numbers is: {result}")