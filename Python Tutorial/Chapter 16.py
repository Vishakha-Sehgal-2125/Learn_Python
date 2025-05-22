# Object Oriented Programming


# Class and Objects
"""
Class: A blueprint or template for creating objects. No memory untill oject is created
It defines a structure and behavior using attributes (data) and methods (functions).
Object: An instance of a class. 
It is created from the class and represents real-world entities.
"""
# Syntax 
"""
class Class_Name:          # Creating class
    Class attributes 
    Class methods 
    pass  # placehorder if necessary
     
object_name = Class_Name()     # Creating an object of the class

""" 
class Animal:   # Define a class named Animal
    
    def make_sound(self):  # Method to define the behavior of the class
        print("The animal makes a sound!")       
print("Bhow")
dog = Animal()  # Create an object of the Animal class
dog.make_sound()  # Calling the make_sound method


class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry" # This is an instance attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)
"""
Here name is instance attribute and salary and language are class attributes 
as they directly belong to the class, we can make instance att. out of the class
"""

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

harry = Employee()
print(harry.language)
harry.language = "JavaScript" # This is an instance attribute
print(harry.language, harry.salary)
""" First Priority will be value of instance attribute if any
Like here harry.language is both class and instance attribute 
but the value will be chosen of instance attribute 
"""
kuhu = Employee()
print(kuhu.language)

# What is self ?
"""
self is a memory reference to the current object of the class.
It is used to access the attributes and methods of the class inside its methods.
In simple words jab bhi hum koi Method create Karte Hain Class Ke Andar Toh Usme Bale hi Hum Koi Bhi Parameter Nahi de 
LeKin Phir Bhi Hame Ek Parameter Jo ki Self hota Hai Woh Dena Parta Hai vrna positional arguement ki error aa jati he
Or usi Self ko use Karke hum attributes ko bhi access Kar Sakte Hai inside that method.
"""
# Code without self 
# class Employee: 
#     language = "Python" 
#     salary = 1200000
#     def getInfo():
#         print(f"The language is {language}. The salary is {salary}")

# harry = Employee()
# harry.getInfo() # Compiler get it as Employee.getInfo(harry) and here there is one arguement and in method we passed nothing.
# Employee.getInfo(harry) 

# Code with self
class Employee: 
    language = "Python" 
    salary = 1200000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.getInfo() # Without self Compiler get it as Employee.getInfo(harry) and here there is one arguement and in method we passed nothing.
# Employee.getInfo(harry) 

# Steps for creating an object
"""
1. Memory allocation for the object 
2. Memory Reference returned to the object
3. Memroy reference (self) automatically passed inside the constructor
4. Constructor (init) creates/initialises variable at the memory reference.
"""

# Constructor in Python
"""
A constructor is a special method in a class that is automatically called when an object of the class is created. 
It initializes the object's attributes and sets up any necessary properties.The constructor in Python is defined 
using the special method __init__. It's called automatically when an object is instantiated.
It can accept arguments to initialize attributes.
"""
# Syntax 
"""class ClassName:
    def __init__(self, parameters):
        # Initialization code
        self.attribute = value
"""

# What is __init__() method or Constructor ?
"""
__init__ is a special method in Python called a constructor. It can take self arg. or any further arg.
It is used to initialize the attributes (variables) of the class.
Without constructor execution obj. create nhi ho skta he.
"""
# Types of Constructors
"""
1. Non-Parameterized Constructor
No parameters are passed to the constructor except self.
Initializes attributes with default values.
2. Parameterized Constructor
Takes arguments to initialize attributes dynamically.
Allows customization when creating objects.
3. Default Constructor
Python doesn't need you to explicitly define a constructor if you're not doing anything special.
It assigns default values to the object.
"""
class Employee: 
    # Class attributes (common to all objects if not overridden)
    language = "Python"  # Default programming language for employees
    salary = 1200000  # Default salary for employees

    # This is a parameterized constructor
    def __init__(self, nm, sal, lang): 
        # __init__ is automatically called when an object is created.
        # It initializes the object with specific attributes.
        print("I am creating an object")  # Message to indicate object creation
        self.name = nm  # Assigning the name provided to the object's 'name' attribute
        self.salary = sal  # Assigning the salary provided to the object's 'salary' attribute
        self.language = lang  # Assigning the language provided to the object's 'language' attribute

    # This is a non-parameterized method
    def getInfo(self): 
        # Prints the language and salary of the object
        print(f"The language is {self.language}. The salary is {self.salary}")

# Creating an object 'harry' of the Employee class
# The values "Harry", 1300000, and "JavaScript" are passed to the parameterized constructor
harry = Employee("Harry", 1300000, "JavaScript")  

# harry.name = "Harry" # Instead of assigning attributes manually like this, 
# we directly provide them as arguments when creating the object (as shown above).

# Accessing and printing object attributes
print(harry.name, harry.salary, harry.language)  # Output: Harry 1300000 JavaScript
harry.getInfo


class Car:
    wheels = 4
    fuel_type = "Petrol"

    def __init__(self, brand, model, price):
        print("A new car object is being created!")
        self.brand = brand
        self.model = model
        self.price = price

    def displayDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price},Wheels: {self.wheels}")

car1 = Car("Toyota", "Corolla", 2000000)
print(car1.brand, car1.model, car1.price)
car1.displayDetails()




class Laptop:
    brand = "Generic"

    def __init__(self, model, price, ram):
        print("A new laptop object is being created!")
        self.model = model
        self.price = price
        self.ram = ram

    def getLaptopInfo(self):
        print(f"Model: {self.model}, Price: {self.price}, RAM: {self.ram}GB")

    def discountPrice(self, discount_percentage):
        discounted_price = self.price - (self.price * discount_percentage / 100)
        print(f"Discounted price: {discounted_price}")

    def upgradeRam(self, new_ram):
        self.ram = new_ram
        print(f"RAM upgraded to: {self.ram}GB")

    def isExpensive(self):
        if self.price > 50000:
            print(f"The {self.model} is expensive!")
        else:
            print(f"The {self.model} is affordable.")

# Creating a laptop object
laptop1 = Laptop("Dell XPS 13", 75000, 16)

# Using different methods
laptop1.getLaptopInfo()
laptop1.discountPrice(10)  # 10% discount
laptop1.upgradeRam(32)  # Upgrading RAM to 32GB
laptop1.isExpensive()
