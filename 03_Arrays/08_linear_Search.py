arr = [1, 2, 3, 4, 5]
num = 3

for i in range(len(arr)):
  if arr[i] == num:
    print(i)
    
# Time Complexity: O(N), where N is the number of elements in the array. This is because we traverse the entire array to find the element.

# Space Complexity: O(1), as we are using a constant

nums = [4, 7, 1, 9]
target = 1

if target in nums:
    print("Found at index", nums.index(target))
