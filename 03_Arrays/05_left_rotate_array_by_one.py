nums = [1, 2, 3, 4, 5]
i = nums[0]
n = len(nums)

for j in range(1,n):
  nums[j-1] = nums[j]

nums[n-1] = i

print(nums) #[2, 3, 4, 5, 1]

# Time Complexity: O(N), where N is the size of the input array. This is because we traverse the array once to shift the elements.

# Space Complexity: O(1), as we are using only a constant amount of extra space for the temporary variable.

