def ri(arr,i=0,n=None):
  if n is None:
    n = len(arr)

  if n == 1:
    return
  
  j = i
  while j>=0 and arr[j-1]> arr[j]:
        arr[j+1] = arr[j]
        j-=1

  ri(arr,i+1,n)
