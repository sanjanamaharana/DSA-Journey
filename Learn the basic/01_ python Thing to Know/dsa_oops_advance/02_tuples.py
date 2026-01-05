# Tuples are ordered but immutable collections (cannot be changed after creation).

a = (1,12,11)
print(a) # (1,12,11)
print(a[1]) # 12
a[2] =12 # can't change give error

my_tuple = (10, 20, 30)
single_element = (5,)  # Tuple with one element (comma required)

n1,n2,n3 = my_tuple
print(n1) # 10







a = (1,12,11,12,13,12)

print(a.count(12)) #3
print(a.index(12)) #1

# Why Use Tuples?
# Faster than lists (since they are immutable)
# Used as dictionary keys (since they are hashable)
# Safe from unintended modifications