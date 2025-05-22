# Inheritance :- Inheritance is an property of creating a new class from an existing class
"""
We can use the method and attributes of Employee in Programmer object.
Also, we can overwrite or add new attributes and methods in Programmer class.
"""
#Syntax
"""
class Employee: # Base class
# Code
class Programmer(Employee): # Derived or child class
# Code
"""


class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

"""
This is one method in which we can just copy the methods or attributes into another class
to acess them or inherit them in that class here is the example,But this is error prone
"""
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


# Single inheritance
class Programmer(Employee):   # Inherited Programmer from employee
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)


# Multiple Inheritance
class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     


class Programmer(Employee, Coder):   # Inherited Programmer from employee and coder
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()


# Multilevel Inheritance 
class Employee:
    a = 1 

class Programmer(Employee):   # Inherited Programmer from employee
    b = 2 

class Manager(Programmer):    # Inherited Manager from Programmer
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)