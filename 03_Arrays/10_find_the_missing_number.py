class Solution:
    # Function to find the missing number
    def missingNumber(self, a, N):
        # Check every number from 1 to N
        for i in range(1, N + 1):
            found = False

            # Linear search to check if i exists in the list
            for num in a:
                if num == i:
                    found = True
                    break

            # If not found, return it as missing
            if not found:
                return i

        # This will never be reached
        return -1

# Driver code
a = [1, 2, 4, 5]
N = 5
obj = Solution()
ans = obj.missingNumber(a, N)
print("The missing number is:", ans)

# Time Complexity: O(N*N), since nested for loops are used

# Space Complexity: O(1). No extra space used














array= [1,2,3,5]
n = 5

if n == len(array):
  print("no missing word")

array.sort()

for i in range(n):
  if array[i+1] != array[i]+1:
    print(array[i+1])
  
# time complexity O(n log n)
# space comexity o(1)














array= [1,2,4,5]
n = 5
sum = n*(n+1)//2
sum_arr = sum(array)
missing_element = sum - sum_arr

print(missing_element)

# Time Complexity: O(N). Single loop is used

# Space Complexity: O(3N) where 3 is for the stack, left small array and a right small array
















class Solution:
    # Function to find the missing number using XOR approach
    def missingNumber(self, a, N):
        xor1 = 0
        xor2 = 0

        # XOR array elements and numbers from 1 to N-1
        for i in range(N - 1):
            xor2 ^= a[i]      # XOR of array elements
            xor1 ^= (i + 1)   # XOR of 1 to N-1

        xor1 ^= N  # Include N in the XOR

        return xor1 ^ xor2  # Missing number

# Driver code
a = [1, 2, 4, 5]
N = 5
obj = Solution()
ans = obj.missingNumber(a, N)
print("The missing number is:", ans)


