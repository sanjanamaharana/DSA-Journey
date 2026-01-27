nums = [-1,0,3,5,9,12]
target = 9


start = 0
end = len(nums) - 1
while(end >= start):
  mid = ((end - start) // 2) + start
  if target < nums[mid]:
    end = mid -1
  elif target > nums[mid] :
    start = mid+ 1
  else:
    print(mid)
    break
print("the number is not in array")