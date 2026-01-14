arr = [5,4,3,2,1]
n = len(arr)
ans = [0] * n 
for i in range(n):
  ans[i] = arr[n-i-1]

print(ans)

# [1, 2, 3, 4, 5] O(n)
# Space Complexity: O(n)

arr = [5,4,3,2,1]
n = len(arr)
for i in range(n//2):
  temp = arr[i]
  arr[i]=arr[n-i-1]
  arr[n-i-1] = temp

print(ans)
# [1, 2, 3, 4, 5] O(n),0(1)


arr = [5,4,3,2,1]
print(arr[::-1])
# [1, 2, 3, 4, 5] O(n),0(n)




class Solution:
    # Function to reverse the array using slicing
    def reverseArray(self, arr):
        # Reassign the array with reversed version using slicing
        arr[:] = arr[::-1]

# Driver code
if __name__ == "__main__":
    # Input array
    arr = [1, 2, 3, 4, 5]

    # Create Solution object
    obj = Solution()

    # Call reverse function
    obj.reverseArray(arr)

    # Output the reversed array
    print(" ".join(map(str, arr)))
# 5 4 3 2 1