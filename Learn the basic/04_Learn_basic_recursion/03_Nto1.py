class solution:
  def name(self,number):
    if(number == 0):
      return
    
    print(number, end=' ')

    self.name( number-1)
if __name__ == "__main__" :
    ss = solution()
    ss.name(5)

# 5 4 3 2 1 

class solution:
  def name(self,number):
    if(number == 0):
      return
    self.name( number-1)
    print(number, end=' ')

    self.name( number-1)
if __name__ == "__main__" :
    ss = solution()
    ss.name(5)

# 1 2 3 4 5 