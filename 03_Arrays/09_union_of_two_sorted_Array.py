
arr1 = [1,2,3,4,5]
arr2= [2,3,4,4,5]

freq = {}

for i in range(len(arr1)):
  freq[arr1[i]] = freq.get(arr1[i],0)+1

for i in range(len(arr2)):
  freq[arr2[i]] = freq.get(arr2[i],0)+1

# union =freq.keys() # dict_keys([1, 2, 3, 4, 5, 9, 0])

union =sorted(freq.keys()) # [0, 1, 2, 3, 4, 5, 9]
print(union)















arr1 = [1,2,3,4,5]
arr2= [2,3,4,4,5]

# set1 = set(arr1)
# set2 = set(arr2)

# union1 = set1.union(set2)

union1 = set(arr1) | set(arr2)

print(union1)


















arr1 = [1,2,3,4,5]
arr2= [2,3,4,4,5]
union = []

i,j = 0,0

while i < len(arr1) and j < len(arr2):
  if arr1[i] < arr2[j]:
    if not union or union[-1] != arr1[i]:
      union.append(arr1[i])
    i += 1
  elif arr1[i] > arr2[j]:
    if not union or union[-1] != arr2[j]:
      union.append(arr2[j])
    j += 1
  else:
    if not union or union[-1] != arr1[i]:
      union.append(arr1[i])

    i += 1
    j += 1

while i < len(arr1):
  if not union or union[-1] != arr1[i]:
      union.append(arr1[i])
  i += 1

while j < len(arr2):
  if not union or union[-1] != arr2[j]:
      union.append(arr2[j])
  j += 1

print(union)
