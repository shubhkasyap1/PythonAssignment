def find_second_max(arr, n):
    if n < 2:
        return None 
    max_element = second_max = float('-inf')
    for i in range(n):
        if arr[i] > max_element:
            second_max = max_element
            max_element = arr[i]
        elif arr[i] > second_max and arr[i] != max_element:
            second_max = arr[i]
    return second_max

n = int(input("Enter the size of the array (n): "))

if n <= 0:
    print("Invalid size. n must be a positive integer.")
else:
    
    arr = [int(input()) for i in range(n)]

    second_max_element = find_second_max(arr, n)
    if second_max_element is None:
        print("The array has less than 2 distinct elements.")
    else:
        print(f"Second highest element in the array: {second_max_element}")
