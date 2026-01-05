a = 23 
print(type(a))  # Output: <class 'int'>

b = "23"
print(type(b))  # Output: <class 'str'>

#  converting b to integer
c= int(b)
print(type(c))  # Output: <class 'int'>

s = "23.45"
print(type(s))  # Output: <class 'str'>
# converting s to float
f = float(s)
print(type(f))  # Output: <class 'float'>

num ="23"
print(num+2) # give Error
print (int(num) + 2 ) #25






# Create a tuple coordinates = (10, 20) and print both elements.
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)
print(type(coordinates))
li = list(coordinates)
print (li)
li[0]= 50
coordinates = tuple(li)
print(coordinates)