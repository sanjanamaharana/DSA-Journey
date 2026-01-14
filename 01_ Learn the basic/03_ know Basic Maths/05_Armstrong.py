n = 153
no = n
a = 0
length = len(str(n))

while(n != 0):
    rem = n % 10
    a = a + (rem ** length)
    n //= 10
if (no == a):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

print(f"Final Sum: {a}")