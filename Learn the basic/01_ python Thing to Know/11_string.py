name1='khusi'

c = '''This is
a multi-line
string.'''
print(c)
# This is
# a multi-line
# string.

name = "san jana"
#       01234567
#      -8     -1
print(name[0]) # s
print(name[1]) # a
print(name[2]) # n
print(name[3]) # space
print(name[8]) # error
print(name[-1]) # a  last element 
print(name[-2]) # n  name[-2+8] name[6]
print(name[-4]) # j

print(name[0:2]) #sa
print(name[:2]) #sa
print(name[2:-1]) #n jan
print(name[2:])   #n jana
print(name[-5: -1]) # jan
print(name[-1: -3]) # give nothing


print(name[0:5:2]) #snj # skip 1 charcter
print(name[:: 2]) # snjn
print(name[:: -1]) #anaj nas # it reverse of word

name3 = "sanju" #immutable
name3[0] = "R"  # you can't do

length = len(name3)
print(length) #5

text = "hello sanjana"

print(text.upper(), text) # HELLO SANJANA , hello sanjana
print(text.lower(), text) # hello sanjana hello sanjana
print(text.capitalize(), text) # Hello sanjana hello sanjana
print(text.title(), text) # Hello Sanjana hello sanjana

text = "  \nhello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: " 
#                                hello world"

text = "Python is fun and fun and fun"
print(text.find("is"))   # Output: 7 1st occurence
print(text.replace("fun", "awesome"))  # Output: "Python is awesome and awesome and awesome"

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False

print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'