# Sets are unordered, unique collections (no duplicates).


fruits = {"apple", "banana", "cherry"}

print(fruits[1]) # give error

print(fruits) # {"apple", "banana", "cherry"}
print(type(fruits)) # <class 'set'>

fruits.add(32)
fruits.add(322.333)
print(fruits) #{32, 'banana', 322.333, 'cherry', 'apple'}

fruits.remove("apple") # apple is not now in the fruit set

fruits.remove("sanju") # sanju is not  in the fruit set so give Error

fruits.discard("sanju") # now don't give Error 

fruits.pop()         # Removes random element







# Set Operations:

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))   # {1, 2}