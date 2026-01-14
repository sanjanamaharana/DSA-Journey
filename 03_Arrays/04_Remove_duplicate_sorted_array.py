arr=[1,1,2,2,2,3,3]

a = set(arr)
print(list(a))
print(len(a))


from collections import Counter

arr = [1,1,2,2,2,3,3]
freq = Counter(arr)
print(freq)


freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)







# leetcode 26

def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0  # index of last unique element

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


# Time Complexity: O(N), We traverse the entire original array only once.
# Space Complexity: O(1), constant additional space is used to check unique elements.








def rem_dup_array(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]
        i += 1
        arr[i] = arr[j]

    return i+1
    
    
    
        
    

