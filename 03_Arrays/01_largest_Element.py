arr = [2, 5, 1, 3, 0]

arr.sort()
print(f" largest number of arr is {arr[-1]}")


# Time Complexity: O(N log N), where N is the size of the array, as we are sorting the array.

# Space Complexity: O(1), as we are using a constant

























arr = [2, 5, 1, 3, 0]

v = max(arr)
print(v)


# Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.

# Space Complexity: O(1), as we are using a constant




# Function to find the largest element in the array
def findLargestElement(arr, n):
    max = arr[0]  # Initialize max with the first element in the array

    # Iterate through the array to find the maximum element
    for i in range(1, n):
        if arr[i] > max:  # If the current element is greater than max, update max
            max = arr[i]

    return max  # Return the largest element found

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