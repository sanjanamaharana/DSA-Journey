import math

list = []
num =12

for i in range(1,int(math.sqrt(num))+1):
  if (num % i == 0):
    list.append(i)
    j = num // i
    list.append(j)
list.sort()
print(list)
