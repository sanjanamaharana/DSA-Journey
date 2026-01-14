
arr = [13,46,24,52,20,9]

for i in range(1,len(arr)):
    j = i -1
    q = arr[i]
    while j>=0 and arr[j]> q:
        arr[j+1] = arr[j]
        j-=1

    arr[j+1] = q

print(arr)

# Time Complexity: O(n^2), where n is the number of elements in the array. This is because, in the worst case, we may have to compare each element with all the previous elements.

# Space Complexity: O(1), as we are sorting the array in place and not using any additional data structures that grow with input size.

