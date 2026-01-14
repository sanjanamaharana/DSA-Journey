class Solution:
    
    def mergeSort(self,arr):
        if (1 >= len(arr)):
            return arr
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        result= []
        i = j = 0
        while( i < len(left) and j <len(right)):
            if (left[i] <= right[j]):
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
   

arr = [5, 2, 8, 4, 1]
sol = Solution()
arr = sol.mergeSort(arr)
print(*arr)


# Time Complexity: O(N*logN), merging two arrays take linear time and array is recursively divided into halves (logN times).
# Space Complexity: O(N), we use a temporary array to store elements in sorted order.
