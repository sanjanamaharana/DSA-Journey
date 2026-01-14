arr = [10,5,10,15,10,5]
n = len(arr)

visited = [0] * n


for i in range(n-1):
  count = 0
  if(visited[i] == 't'):
    continue
  for j in range(i,n):
    if arr[i] == arr[j]:
      visited[j] ='t'
      count +=1
    
  print(arr[i],count)
  
# Time Complexity: O(N²), as for every element we may scan the remaining elements in the array.

# Space Complexity: O(N), for the visited array of size N.

arr = [10, 5, 10, 15, 10, 5]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    print(key, value)


# 10 3
# 5 2
# 15 1

# Time Complexity: O(N), where N is the number of elements in the array. Each element is processed once.

# Space Complexity: O(N), for storing frequencies of unique elements in the unordered_map.

from collections import defaultdict

class Solution:
    # Function to count frequency of each element in the array using defaultdict
    def Frequency(self, arr, n):
        # Create a defaultdict to store frequency of each element
        freq_map = defaultdict(int)

        # Traverse the array and count frequencies
        for i in range(n):
            freq_map[arr[i]] += 1

        # Traverse through the defaultdict and print frequencies
        for key, value in freq_map.items():
            print(key, value)

if __name__ == "__main__":
    # Input array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    # Create Solution instance
    sol = Solution()

    # Call the function to count frequencies
    sol.Frequency(arr, n)
