def print_fibonacci(n):
    a, b = 0, 1
    print(a, " ", b, end=" ")
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(" ", c, end=" ")
    print()

n = int(input("Enter any number: "))

print_fibonacci(n)