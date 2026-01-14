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


arr = "sanj :ana # a Na jnA s"

left ,right = 0 , len(arr)-1

while(left < right):
   if(not arr[left].isalnum()):
      left = left +1
   elif not arr[right].isalnum():
      right -=1

   elif arr[left].lower() != arr[right].lower():
      print(False)
   else:
      left+=1
      right-=1
print(True)

# # True
# Time Complexity: O(N), where N is the length of the string. Each character is compared at most once till the middle of the string.

# Space Complexity: O(1), since no extra space is used apart from a few variables for iteration.

class solution:
   def pali(self,arr,left,right):
      self.arr = arr

      if(left > right):
         return True
      
      elif(not arr[left].isalnum()):
         left = left +1
      elif not arr[right].isalnum():
         right -=1

      elif arr[left].lower() != arr[right].lower():
         return False

      return self.pali(arr,left+1,right-1)


ss = solution()
arr = "sanj :ana # a Na jnA s"
e = ss.pali(arr,0,len(arr)-1)
print(e)

















# Function to check if a string is a palindrome using recursion
def palindrome(i, s):
    # Base Condition: If i exceeds half of the string, all the elements have been compared
    # and the string is a palindrome, return True.
    if i >= len(s) // 2:
        return True

    # If the start and end characters are not equal, it's not a palindrome.
    if s[i] != s[len(s) - i - 1]:
        return False

    # If both characters are the same, increment i and check start+1 and end-1.
    return palindrome(i + 1, s)

# Driver code
if __name__ == "__main__":
    s = "sanj :ana # a Na jnA s"  # Example string to check
    
    # Check if the string is a palindrome and output the result
    print(palindrome(0, s))  # Output True if palindrome, False if not









def palindrome(left, right, s):
    if left >= right:
        return True

    if not s[left].isalnum():
        return palindrome(left + 1, right, s)

    if not s[right].isalnum():
        return palindrome(left, right - 1, s)

    if s[left].lower() != s[right].lower():
        return False

    return palindrome(left + 1, right - 1, s)


if __name__ == "__main__":
    s = "sanj :ana # a Na jnA s"
    print(palindrome(0, len(s) - 1, s))
