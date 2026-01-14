class solution:
  def name(self,count,number):
      

      if(count > number):
          return 0
      a = self.name(count + 1,number) 
      sum = a+ count
      
      return sum
       
if __name__ == "__main__" :
    ss = solution()
    w=ss.name(1,5)
    print(w) #15


class solution:
  def name(self,number):
      

      if(number == 1):
          return 1
      a = self.name(number-1) 
      sum = number+a
      
      return sum
       
if __name__ == "__main__" :
    ss = solution()
    w=ss.name(1,5)
    print(w) #15


    