i = 1
while(i<10):
  print(i)
  i+=1


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Use a while loop to reverse a given number (e.g., 123 → 321).

a = 123
i =1
rev = 0
while(a!=0):
  rem = a % 10
  rev = (rev*10) + rem
  a = a // 10
print(rev) #321


# Write a program that keeps asking the user to enter a password until they enter the correct one

passw = 123
while(passw):
  b = int (input("enter the password : "))
  if(passw == b):
    print("correct")
    break
