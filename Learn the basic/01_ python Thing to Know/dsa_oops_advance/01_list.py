# Lists are ordered, mutable (changeable) collections of items.

numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14,False]

print(numbers) # [1, 2, 3, 4, 5]
print(numbers[3]) # 4
numbers[3] = 8
print(numbers) # [1, 2, 3, 8, 5]
print(numbers[5]) # Error index out of bound
print(mixed[2:4]) # ["hello", 3.14]


  



my_list = [1, 2, 3]

my_list.append(4)   # [1, 2, 3, 4]
my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
my_list.remove(2)   # [1, 99, 3, 4]
my_list.pop()       # Removes last element -> [1, 99, 3]
my_list.reverse()   # [3, 99, 1]
my_list.sort()      # [1, 3, 99]
my_list.extend(mixed)  # [1, 3, 99, 10, "hello", 3.14,False]







a = 5
table = []

for i in range(1,11):
  table.append(a*i)
print(table) #[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# same 

squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]



fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(len(fruits))

fruits[2] = "orange"