class solution:
  def name(self,number):
      

      if(number == 0):
          return 1
      return number * self.name(number-1)
       
if __name__ == "__main__" :
    ss = solution()
    w=ss.name(5)
    print(w) #120
