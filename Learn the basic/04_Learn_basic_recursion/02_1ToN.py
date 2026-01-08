class solution:
  def name(self,count,number):
    if(count > number):
      return
    
    print(count, end=' ')

    self.name( count+1,number)
if __name__ == "__main__" :
    ss = solution()
    ss.name(1,5)
# 1 2 3 4 5 


class solution:
  def name(self,count,number):
    if(count > number):
      return
    self.name( count+1,number)
    print(count)

    
if __name__ == "__main__" :
    ss = solution()
    ss.name(1,5)

# 5
# 4
# 3
# 2
# 1

