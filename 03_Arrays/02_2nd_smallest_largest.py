arr = [2, 5, 1, 3, 0]
arr.sort()
a =  list(set(arr))
print(a[1],a[-2])

# Time Complexity: O(N log N), for sorting the array.

# Space Complexity: O(1), as we are using a constant amount of space for variables.


















def findLargestElement(arr, n):
    max = float('-inf')  # Initialize max with the first element in the array
    mini = float('inf')
    smax = float('-inf')
    smini = float('inf')

    # Iterate through the array to find the maximum element
    for i in range(1, n):
        if arr[i] > max:  # If the current element is greater than max, update max
            max = arr[i]
        if arr[i] < mini:  # If the current element is greater than max, update max
            mini = arr[i]

    for i in range(n):
        if arr[i] >smax and arr[i] != max :
            smax = arr[i]
        elif arr[i] <smini and arr[i] != mini :
            smini = arr[i]

        

    return smax,smini  # Return the largest element found

# Driver code
if __name__ == "__main__":
    # Array 1
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)  # Size of the array
    max = findLargestElement(arr1, n)  # Call the function to find the largest element
    print("The largest element in the array is:", max)  # Output the result

    # Array 2
    arr2 = [8, 10, 5, 7, 9]
    n = len(arr2)  # Size of the array
    max = findLargestElement(arr2, n)  # Call the function to find the largest element
    print("The largest element in the array is:", max)  # Output the result

# Time Complexity: O(N), we do two linear traversals in our array.

# Space Complexity: O(1), as we are using a constant amount of space for variables.






















def findLargestElement(arr, n):
    max = float('-inf')  # Initialize max with the first element in the array
    mini = float('inf')
    smax = float('-inf')
    smini = float('inf')

    # Iterate through the array to find the maximum element
    for i in range(1, n):
        if arr[i] > max:  # If the current element is greater than max, update max
            max = arr[i]
        if arr[i] < mini:  # If the current element is greater than max, update max
            mini = arr[i]

    for i in range(n):
        if arr[i] >smax and arr[i] != max :
            smax = arr[i]
        elif arr[i] <smini and arr[i] != mini :
            smini = arr[i]

        

    return smax,smini  # Return the largest element found

# Driver code
if __name__ == "__main__":
    # Array 1
    arr1 = [2, 5, 1, 3, 0]
    n = len(arr1)  # Size of the array
    max = findLargestElement(arr1, n)  # Call the function to find the largest element
    print("The largest element in the array is:", max)  # Output the result

    # Array 2
    arr2 = [8, 10, 5, 7, 9]
    n = len(arr2)  # Size of the array
    max = findLargestElement(arr2, n)  # Call the function to find the largest element
    print("The largest element in the array is:", max)  # Output the result

# Time Complexity: O(N), we do two linear traversals in our array.

# Space Complexity: O(1), as we are using a constant amount of space for variables.






























def secondMaxAndMin(arr):
    if len(arr) < 2:
        return None, None

    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x != max1 and x > max2:
            max2 = x

        if x < min1:
            min2 = min1
            min1 = x
        elif x != min1 and x < min2:
            min2 = x

    return max2, min2


# Time Complexity: O(N), we do two linear traversals in our array.

# Space Complexity: O(1), as we are using a constant

