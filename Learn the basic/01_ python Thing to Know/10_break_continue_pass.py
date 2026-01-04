for i in range(0,21):
  print(i)
  if (i == 5):
    break
# 0
# 1
# 2
# 3
# 4
# 5

for i in range(0,21):
  if (i == 5):
    break
  print(i)
# 0
# 1
# 2
# 3
# 4
for i in range(0,10):
  print(i)
  if (i == 5):
    continue
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(0,10):
  if (i == 5):
    continue
  print(i)
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9


i = 3
if i == 12:
  print("s") #not show
  pass
  print("s") #not show
print("sa") #sa

# Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
for i in range(1, 6):
    match i:
      case 1 :
        print(1)
      case 2 :
        print(2)
      case 3 :
        pass
      case 4 :
        print(4)
      case 5 :
        print(5)
# 1
# 2
# 4
# 5

for i in range(1, 6):
    if i == 3:
        pass      # Does nothing when i is 3
    else:
        print(i)  # Only prints if i is NOT 3
