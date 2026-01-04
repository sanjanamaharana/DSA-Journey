def sum(a,b):
  d = a + b
  print(d)

def sum1(a,b):
  d = a + b
  return d

def sum2():
  print("sum")


num1= 12
num2 = 12
sum(num1,num2)

s = sum1(num1,num2)
print(s)


sum2()

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!


def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")

def mul(a,b):
   c = a*b
   return c

multi = mul(b= 30, a = 2)
print(multi)

sq = lambda x: x*x

print(sq(3))  # 9

avg = lambda x,y : (x+y)//2
print(avg(3,5))  # 4
# or
'''
 def avg(x,y):
    return (x+y)//2
'''
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]







#  RECURSION 

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120

def sum_of_digits(n):
    # Base Case: if n is a single digit, return n
    if n < 10:
        return n
    else:
        # Recursive Step: last digit + sum of remaining digits
        return (n % 10) + sum_of_digits(n // 10)
                  # 5 + sum_of_digits(12)
                  # 7+ sum_of_digits(1)
                  # 8

# Test the function
number = 125
print(f"The sum of digits in {number} is: {sum_of_digits(number)}")





# Modules and pip - Using External Libraries

# build in modules like math and search in google
import math
import os
print(math.sqrt(16))


# external module
import hello_module

hello_module.hello()





# Installing External Libraries with pip
#                                             pip install requests

# Example usage:

import requests
 
response = requests.get("https://api.github.com")
print(response.status_code)

r = requests.get("https://www.google.com")
print(r.text)




x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print(x)  # Output: 5

my_func()
print(x)  # Output: 10 (global x remains unchanged)

x = 10  # Global variable

def modify_global():
    global x
    x = 5  # Modifies the global x  # here var is not used

modify_global()
print(x)  # Output: 5

# 1. question
def ss():
    c = 12
    global z  # This tells Python: "When this runs, make z available everywhere"
    z = 3
    return c + z

# 1. Call the function so the 'global z' line actually runs
ss() 

# 2. Now z exists in the global scope
print(z + 2)  # Output: 5







def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)  # Output: Returns the sum of two numbers.


# triple qotatio comment only show __doc__ , even # single line comment not work here.

def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b








# def sqr(num):
#     return num*num
    
# sqr = lambda x : x*x
import math
print(pow(4,2))
    
# print(sqr(4))