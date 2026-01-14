arr = [5, 2, 8, 4, 1]

for i in range(0,len(arr)//2):
  j = arr(len(arr)-1)
  
  if arr[i] > arr[j]:
    arr[i],arr[j] = arr[j],arr[i]
    i += 1
  else:
    j += 1




# Online Python compiler (interpreter) to run Python online.
arr = [5, 2, 8, 4, 1]
i = 0
j = len(arr)-1
while(i<=j):
  if arr[i] > arr[j]:
    arr[i],arr[j] = arr[j],arr[i]
    i += 1
  if(j == i):
      j -= 1
j -= 1
print(arr)