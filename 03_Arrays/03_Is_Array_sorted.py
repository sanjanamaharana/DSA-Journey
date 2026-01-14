arr = [1,2,3,4,5]

a = arr
a.sort()
if(a == arr):
  print(True)
else:
  print(False)





for i in range(len(arr)-1):
  if(arr[i] <= arr[i+1]):
    print(True)
    break
  else:
    print(False)
    break


# Time Complexity: O(N), as it checks each adjacent pair once in a single pass through the array.

# Space Complexity: O(1), as it uses constant extra space regardless of input size.















# 1752 leetcode


def check(nums):
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
            if count > 1:
                return False

    return True
