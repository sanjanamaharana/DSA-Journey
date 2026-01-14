age = 23 # integer
cgpa = 8.99 # float
name = "Sanjana" # string
is_online = True # boolean
list1 = [1, 2, 3] # list ordered,mutable,allows duplicates
tuple1 = (1, 2, 3) # tuple ordered,immutable,allows duplicates
set1 = {1, 2, 3} # set unordered,mutable,no duplicates
dict1 = {"name": "Sanjana", "age": 23} # dictionary unordered,mutable,key-value pairs

print("Hello! My name is ",name," and Age:", age,".my cgpa is ", cgpa)
# Hello! My name is  Sanjana  and Age: 23 .my cgpa is  8.99


age = 23 # integer
cgpa = 8.99 # float
name = "Sanjana" # string
is_online = True # boolean
list1 = [1, 2, 3] # list ordered,mutable,allows duplicates
tuple1 = (1, 2, 3) # tuple ordered,immutable,allows duplicates
set1 = {1, 2, 3} # set unordered,mutable,no duplicates
dict1 = {"name": "Sanjana", "age": 23} # dictionary unordered,mutable,key-value pairs

print("Hello! My name is ",name," and Age:", age,".my cgpa is ", cgpa)
# Hello! My name is  Sanjana  and Age: 23 .my cgpa is  8.99

print("Hello! My name is "+name+" and Age:"+ age+".my cgpa is "+ cgpa) 
#give Error

print("Hello! My name is "+name+" and Age:"+ str(age)+".my cgpa is "+ str(cgpa))
# Hello! My name is Sanjana and Age:23.my cgpa is 8.99


print(type(age))

# start with (a-z , A-Z),underscore(_)
# variable have letters,number,no spaces, no special characters
# case sensitive age Age AGE aGE _age are different variables

