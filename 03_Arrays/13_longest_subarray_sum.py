nums = [10, 5, 2, 7, 1, 9]
k = 15

count = 0
longa =  0

for i in range(len(nums)):
  sum = nums[i]
  for j in range(i+1,len(nums)):
    sum += nums[j]
    count += 1
    if sum == k:
        
        length = j - i + 1
        if count > longa:
            longa = count
      
print(length)
# brute-force solution (O(n²))






















nums = [10, 5, 2, 7, 1, 9]
k = 15


left = 0
current_sum = 0
longest = 0

for right in range(len(nums)):
   current_sum += nums[right]

   while current_sum > k:
      current_sum -= nums[left]
      left += 1

   if current_sum == k:
      longest = max(longest,right-left+1)

print(longest)

# 4