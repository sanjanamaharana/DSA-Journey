arr = [1,2,3,2,1]
a = arr
n = len(arr)
ans = [0] * n 
for i in range(n):
  ans[i] = arr[n-i-1]
if(a == ans):
    print("palindrome")
    
else:
    print("no")