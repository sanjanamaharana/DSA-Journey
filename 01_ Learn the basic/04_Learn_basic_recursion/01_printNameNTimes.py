class solution:
  def name(self,name,count,number):
    if(count == number):
      return
    
    print(name)

    self.name(name, count+1,number)



ss = solution()
ss.name("sanjana",0,5)

# sanjana
# sanjana
# sanjana
# sanjana
# sanjana