prices = [1, 1, 0, 1, 1, 1]
prices1 = [1, 0, 1, 1, 0, 1
]

count = 0 
max_count = 0

for x in prices:
  if x == 1:
    count += 1
    if count > max_count:
      max_count = count
  else:
    count = 0

print(max_count)



# Time Complexity: O(N), since we scan the array once.

# Space Complexity: O(1), as only constant extra variables are used.

