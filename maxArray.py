def find_max(arr):
    # Initialize max_element
    max_element = arr[0]
    
    # Traverse through the array starting from the second element
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    
    return max_element

n = int(input("Enter the size of the array: "))
arr = []

# Taking array input from the user
for i in range(n):
    element = int(input())
    arr.append(element)

print("The Highest element in the array is:", find_max(arr))
