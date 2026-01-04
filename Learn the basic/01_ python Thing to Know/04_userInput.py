a = input("Enter your name: ")
print(a)

b = input("Enter your CGP:")
print(b)

c = input()
print(c)  #you can do it ,with out prompt

num1 = input("Enter 1st number : " ) #11
num2 = input("Enter 2nd number : ")  #10
ans = num1 + num2 
print(ans) #1110

num1 = int(input("Enter 1st number : " )) #11
num2 = int(input("Enter 2nd number : "))  #10
ans = num1 + num2 
print(ans) #21

num1 = input("Enter 1st number : " )  #"11"
num2 = input("Enter 2nd number : ")   #"10"
ans = int(num1 )+int(num2) #11+10
print(ans)  #21

'''
it is multi label comment
hfufhufufu
dkkdmkvmkd
vkjfvnfjvfjv
'''

#  \n next line
print("sanjanan \\ sank")

# \t new tab
# \' i need ' in my sentence

print("ans","sdmdksmd") #ans sdmdksmd
print("ans" "sdmdksmd") #anssdmdksmd

print("ans","sdmdksmd",7) #ans sdmdksmd 7

# print("ans" "sdmdksmd" 7) 
#ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 2
#     print("ans" "sdmdksmd" 7)
#           ^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("ans","sanjana", 23 , sep=",") # ans , sanjana , 23 
print("ans","sanjana", 23 , sep="/") # ans / sanjana / 23 

print("sanjana")
print("maharana")
# sanjana
# maharana

print("sanjana", end=",")
print("maharana")
# sanjana,maharana

print("sanjana", end="..")
print("maharana", end="//")
# sanjana..maharana//

print('Hello "Python" World!\nThis is on a new line.\nThis is a tab →\tafter tab.')
'''
Hello "Python" World!
This is on a new line.
This is a tab →	    after tab.
'''