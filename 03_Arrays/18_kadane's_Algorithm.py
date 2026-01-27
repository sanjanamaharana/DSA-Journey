nums = [2, 3, 5, -2, 7, -4]  # 15
nums = [-2, -3, -7, -2, -10, -4]     # -2
nums = [-2, -3, -7, -1, -10, -4]    # -1

sum = 0
max = float('-inf')

i = 0
for j in range(len(nums)):
  sum += nums[j]
  if sum > max:
    max = sum
  if sum < 0:
      sum = 0 

print(max)