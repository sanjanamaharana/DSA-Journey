arr = [1, 0, 2, 1, 0]

count0 = count1 = count2 = 0

for i in arr:
  if i == 0:
    count0 += 1
  elif i == 1:
    count1 += 1
  else :
    count2 += 1

index = 0
for i in range(count0):
  arr[index] = 0
  index += 1

for i in range(count1):
  arr[index] = 1
  index += 1

for i in range(count2):
  arr[index] = 2
  index += 1

print(arr)
# [0, 0, 1, 1, 1, 1, 2, 2, 2]

# Time Complexity: O(n),We traverse the array twice: once to count, once to overwrite. Each operation is O(n).

# Space Complexity: O(1), We use only a constant number of counters regardless of the input size. No extra array is used.

















arr = [2, 0, 2,1, 1, 0]

high = len(arr) -1
mid=0
low = 0

while(mid <= high):
  if arr[mid] == 2:
    arr[mid] , arr[high] = arr[high] ,arr[mid]
    high -= 1
  elif arr[mid] == 0:
    arr[mid] , arr[low] = arr[low] ,arr[mid]
    low += 1
    mid += 1
  else:
    mid += 1

print(arr)
# [0, 0, 1, 1, 2, 2]

# Time Complexity: O(n) The array is traversed only once using the `mid` pointer. Each element is checked at most once, and swaps are done in constant time.

# Space Complexity: O(1) Only a few integer pointers (`low`, `mid`, `high`) are used. Sorting is done in-place, requiring no additional space.

