nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

count = 0

for i in range(len(nums)):
  for j in range(i,len(nums)):
    if nums[i] == nums[j]:
      count += 1
  if count > len(nums)//2:
    
    maxi = nums[i]
  count = 0
print(maxi) #7
# Time Complexity: O(N^2), where N is the size of the input array. This is because we are using a nested loop to count the occurrences of each element.

# Space Complexity: O(1), as we are using a constant amount of space for the counters and indices.

















nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

dis = {}
count = 0
for i in range(len(nums)):
  dis[nums[i]] = dis.get(nums[i] , 0)+1

for key,count in dis.items():
  if count > len(nums)//2:
    print(key)

# Time Complexity: O(N), where N is the size of the input array. This is because we are iterating through the array once to count occurrences and then iterating through the hashmap to find the majority element.

# Space Complexity: O(N), as we are using a hashmap to store the counts of each element, which can take up to N space in the worst case



















nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

count = 0
element = 0

for i in range(len(nums)):
  if nums[i] == element:
    count += 1
  else:
    count -= 1
    if count == 0:
      element = nums[i]
      count += 1

print(element)