nums = [1, 2, 3, 4, 5]
k = 2
right = nums[-k:]
left = nums[:k]
n = len(nums)
u = input("choose right or left : ")

if (u == right):
    
    for j in range(n-k-1,-1,-1):
      nums[j+k] = nums[j]

    for i in range(k):
      nums[i] = right[i]

else:
   for j in range(k,n):

    nums[j-k] = nums[j]

   for i in range(k):
    
    nums[n-k+i] = left[i]
   

print(nums)