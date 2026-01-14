class Employee:
  company ="Dell"

  def __init__(self,salary,name,bond,company):
    self.salary = salary  # create an instance attribute of name salary and assign it with salary
    self.name = name
    self.bond1 = bond
    self.company = company

  def get_salary(self):
    return self.salary
  
  def get_info(self):
    print(f"The name of  the employee is {self.name}. salary is {self.salary}. the bond is for {self.bond1} years")


e1 = Employee(64000, "sanjana", 4, "tesla")
# print(e1.get_salary())
e1.get_info() # The name of  the employee is sanjana. salary is 64000. the bond is for 4 years

print(e1.company) # tesla    # it is instance attribute  
print(Employee.company) # Dell   # class attribute

print(dir(e1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bond', 'company', 'get_info', 'get_salary', 'name', 'salary']