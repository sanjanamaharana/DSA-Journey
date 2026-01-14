arr = [13,46,24,52,20,9]
for i in range(len(arr)):
  for j in range(0,len(arr)-i-1):
    if arr[j] > arr[j+1]:
      a = a[j]
      a[j] = a[j+1]
      a[j+1] = a
print(arr)


class BubbleSort:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n - 1, -1, -1):
            for j in range(i):  #Use two nested loops to iterate over the array
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  #Swap arr[j+1] with arr[i]
        
        print("After Using Bubble Sort:")
        print(" ".join(map(str, arr)))


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Using Bubble Sort:")
    print(" ".join(map(str, arr)))

    sorter = BubbleSort()
    sorter.bubble_sort(arr)

# Time Complexity: O(N2), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1).










arr = [13,46,24,52,20,9]
for i in range(len(arr)):
  swap = False
  for j in range(0,len(arr)-i-1):
    if arr[j] > arr[j+1]:
      a = a[j]
      a[j] = a[j+1]
      a[j+1] = a
      swap = True
  if not swap :
     break
print(arr)
# Time Complexity: O(N), (where N = size of the array), for the worst, and average cases.
# Space Complexity: O(1).

