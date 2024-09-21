n = int(input("Enter number of rows: "))

row = 1
while row <= n:
    # Print leading spaces
    col = 1
    while col <= n - row:
        print(" ", end="")
        col += 1
    
    # Print stars
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    
    print()
    row += 1