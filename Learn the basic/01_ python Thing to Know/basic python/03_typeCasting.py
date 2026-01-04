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