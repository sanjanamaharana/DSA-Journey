arr = [2,6,5,8,11]
target = 14

for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[i] + arr[j]== target:
      print("yes")
      exit()
else:
  print("no")
  
# Time Complexity: O(N²) because we use two nested loops to check every possible pair of elements in the array, where N is the size of the array.

# Space Complexity: O(1) as we use a constant amount of extra space regardless of input size.



















arr = [2,6,5,8,11]
target = 14

seen = set()

for i in range(len(arr)):
    rem = target - arr[i]
    if rem in seen:
        print(i, "yes")
        break
    seen.add(arr[i])

# set is best but dict

class Solution:
    def two_sum(self, arr, target):
        seen = {}
        for i, num in enumerate(arr):
            rem = target - num
            if rem in seen:
                return True, [seen[rem], i]
            seen[num] = i
        return False, [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    exists, indices = sol.two_sum(arr, target)
    print("YES" if exists else "NO")
    print(indices)

# Time: O(n)
# Space: O(n)
















arr = [2,6,5,8,11]
sum = 14

right = len(arr)- 1
left = 0
while (left < right):
   if arr[left] + arr[right] > sum:
      right -= 1
   if arr[left] + arr[right] < sum:
      left += 1
   if arr[left] + arr[right] == sum:
      print("yes")
      break
else:
   print("no")

# time complexity = O(n log n)
#  space = o(n)