def print_z_pattern(n):
    if n < 3:
        print("Size should be 3 or greater to form a Z pattern.")
        return
    
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print() 

n = int(input("Enter the size of the pattern (>= 3): "))

print_z_pattern(n)