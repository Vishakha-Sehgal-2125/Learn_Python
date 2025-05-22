# Object Oriented Programming


# class members :- Attributes(variables) + Actions(methods)
# We can access these class members using object outside the class
# Accesing attribute :- object_name.variable_name
# Accessing method :- object_name.method_name()


# Built in class functions:-

# getattr(object_name,attribute_name) :- This gives the value of attribute
# setattr(object_name,attribute_name,new_value) :- This updates the value of attribute with the new value
# delattr(object_name,attribute_name) :- This deletes the value of attribute
# hasattr(object_name,attribute_name) :- This gives a boolean value of True if the object have that attribute
# isinstance(object_name,class_name) :- This gives a boolean value of true if object belongs to the class.

class Employee:
    """This is a documenting string that tells about this class"""
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    """This is not a documenting string """    

e1=Employee("Vishakha",22)
e2=Employee("Kuhu",21)
print(getattr(e1,"age"))    
setattr(e2,"name","Shivansh")
print(e2.__dict__)    
delattr(e2,"age") 
print(e2.__dict__) 
print(hasattr(e2,"age"))
print(isinstance(e1,Employee))


# Buit-in class attributes:-

# __dict__   :- dictionary containing classe's namespace, including all attributes and methods.
# __doc__    :- class documenting string , if provided.
# __name__   :- class name
# __module__ :- module namein which class is defined
# __bases__  :- list of base classes

class Animal:
    """
    This is the Animal class documentation string (docstring).
    It describes the purpose of this class.
    """
    kingdom = "Animalia"  # A class attribute

    def __init__(self, species, habitat):
        self.species = species  # Instance attribute
        self.habitat = habitat  # Instance attribute

print(Animal.__dict__)
print(Animal.__doc__)
print(Animal.__name__)
print(Animal.__module__) # For example, it will display "__main__" if the class is in the main script.
print(Animal.__bases__) # For classes without inheritance, it returns an empty tuple.
"""In Python, all classes implicitly inherit from the object class unless specified otherwise. 
This is why you often see something like:"""

