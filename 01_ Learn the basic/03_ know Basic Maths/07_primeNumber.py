import math

c =0
num =121

for i in range(2,int(math.sqrt(num))+1):
  if (num % i == 0):
      c += 1
      
if(c == 0):
    print("yes")
    
else:
    print("no")




a=5
count =0
for i in range (2,int(a**0.5)+1):
  if a%i==0 :
     count +=1
if count==0:
  print ("true")
else :
     print ("false")