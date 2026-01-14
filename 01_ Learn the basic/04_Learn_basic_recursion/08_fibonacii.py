def main():
    n = 5

    # Edge case: if n is 0, print only 0
    if n == 0:
        print(0)
    # Special case: if n is 1, print first two Fibonacci numbers
    elif n == 1:
        print("0 1")
    # General case: compute and print Fibonacci series
    else:
        fib = [0] * (n + 1)  # List to store Fibonacci numbers
        fib[0] = 0
        fib[1] = 1

        # Fill the list using bottom-up dynamic programming
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        print(f"The Fibonacci Series up to {n}th term:")
        print(" ".join(str(num) for num in fib))

if __name__ == "__main__":
    main()



class solution:
  def fib(self,n):
    if (n == 0):
      return 0
    if (n == 1):
      return 1
    return self.fib(n-1) + self.fib(n-2)
  
ss = solution()
e = ss.fib(5)
print(e)
    
    
a = 0
b =  1
n = 5

while (n > 0):
  sum = a+b
  print(a)
  a = b
  b = sum
  n -=1


# 0112358