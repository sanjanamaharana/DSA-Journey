# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

class Employee:
  company = "hp"

  def salary(self): # self is important here because self is a way to reference the object of class which is being created
    return 34000
  
  def salary1(self): # self is important here because self is a way to reference the object of class which is being created
    print("sanja")
  

e = Employee() #an Object of class Employee is create here
print(e.salary()) # employee e's get salary method is called

e2 = Employee()
print(e2.salary()) # 34000
print(e2.company) #hp
print(Employee.company) #hp
e2.salary() # sanja



















class Dog:  # We define a class called "Dog"
    species = "Canis familiaris" # A class attribute (shared by all Dogs)

    def __init__(self, name, breed):  # The constructor (explained later)
        self.name = name     # An instance attribute to store the dog's name
        self.breed1 = breed   # An instance attribute to store the dog's breed

    def bark(self):          # A method (an action the dog can do)
        print(f"{self.name} says Woof!")

# Now, let's create some Dog objects:
my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object called my_dog
another_dog = Dog("Lucy", "Labrador")     # Creating another object

# We can access their attributes:
print(my_dog.name)       # Output: Buddy
print(another_dog.breed)  # Output: Labrador

# And make them perform actions:
my_dog.bark()            # Output: Buddy says Woof!
print(Dog.species)       # Output: Canis familiaris

# self Explained: Inside a class, self is like saying "this particular object." It's a way for the object to refer to itself. It's always the first parameter in a method definition, but Python handles it automatically when you call the method. You don't type self when calling the method; Python inserts it for you.

# Class vs. Instance Attributes:

# Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.
# Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.