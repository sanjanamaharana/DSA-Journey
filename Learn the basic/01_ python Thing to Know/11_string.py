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

_text = "Python is fun and fun and fun"
print(_text.find("is"))   # Output: 7 1st occurence
print(_text.count("n"))   # 6
print(_text.replace("fun", "awesome"))  # Output: "Python is awesome and awesome and awesome"

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

format_sentence = "sanjana {}  maharana"
s1 = format_sentence.format(name1)
print(s1)

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age)) #My name is Alice and I am 30 years old.
  

# f-Strings (Formatted String Literals)
print (f"My name is {name} and I am {age} years old.") # My name is Alice and I am 30 years old.

x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")

text = "Python"
print(f"{text:>10}")  # Right align  #    Python.
print(f"{text:<10}")  # Left align   #Python    .
print(f"{text:^10}")  # Center align #  Python  .    

# 1. Create a string variable name with your full name. Print:
# The first word
# The last word
# The length of the string

name ="sanjana maharana"
print(name[0:7]) #sanjana
print(name[8:]) #maharana
print(len(name)) #16

# 2.Concatenate two strings: "Hello" and "World" with a space in between.
n1 = "Hello"
n2 = "World"
print(n1 + " " + n2)

text = "Python Programming" # Given text = "Python Programming", do the following:
print(text[0:6]) # Print the first 6 characters
print(text[-6: ]) # Print the last 6 characters
print(text[: :2])# Print every second character from the string




# Write a program that counts how many vowels are in a given string.
sentence = "Coding in Python is fun"
vowel = ['a','e','i','o','u']
sum = 0

for i in sentence:
  if(i in vowel):
    sum += 1
print(f"total vowel is {sum}")

# Take a user input string and check if it is a palindrome (same forwards and backwards).
st = input("Enter a string : ")
rev =st[::-1]
if(st==rev):
  print(f"{st} is a palindrome .because in backward is {rev}")