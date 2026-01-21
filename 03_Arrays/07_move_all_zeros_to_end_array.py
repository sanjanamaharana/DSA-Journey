nums= [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

another = [0] * len(nums)
r = 0
for i in range(len(nums)):
    if(nums[i] != 0):
        another[r] = nums[i]
        r += 1
            
print(another)

# Time Complexity: O(N), we can move all zeroes to end in linear time.
# Space Complexity: O(N), additional space used for temporary array.


nums = [1, 0, 2, 3, 0, 4, 0, 1]

j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

print(nums)