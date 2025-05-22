# SUPER FUNCTION 
"""
super() method is used to access the methods of a super class in the derived class.
It is used within the child class to explicitly call a method from the parent class.
super() is especially useful when:
You override a method in the child class and still want to call the parent's version.
"""
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 
# o = Programmer()
# print(o.a, o.b)
o = Manager()
print(o.a, o.b, o.c)



# WALRUS OPERATOR 
"""
The walrus operator (:=) in Python, introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. 
This can make your code more concise and readable by combining variable assignment and use in a single line.
"""
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
    # Output: List is too long (5 elements, expected <= 3)

# Without walrus
nums = [1, 2, 3, 4, 5]
threshold = 3

filtered_nums = []
for num in nums:
    if num > threshold:
        filtered_nums.append(num)

print(filtered_nums)

# With walrus
nums = [1, 2, 3, 4, 5]
threshold = 3

filtered_nums = [num for num in nums if (value := num) > threshold]

print(filtered_nums)



# TYPES DEFINITIONS
""" 
While Python is a dynamically typed language (you don't have to declare variable types explicitly), 
type hints provide a way to define expected data types for better readability, error-checking, and maintaining code.
Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.
"""
age: int = 25  # Variable type hint
def greeting(name: str) -> str:  # Function type hints
    return f"Hello, {name}!"

print(greeting("Alice")) # Output: Hello, Alice!

def add_numbers(a: int, b: int) -> int:
    return a + b

"""Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.
You can import List, Tuple and Dict types from the typing module like this: """

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid

#Using List and Dict from the typing module to specify the types clearly:
"""
If you pass something like data = [("apple", "three"), ("banana", 5)], your IDE will warn you because "three" is not an int.
"""
from typing import List, Tuple, Dict

def process_records(records: List[Tuple[str, int]]) -> Dict[str, int]:
    result = {}
    for record in records:
        key = record[0]
        value = record[1]
        result[key] = value * 2
    return result

data = [("apple", 3), ("banana", 5), ("cherry", 2)]
print(process_records(data))  # Output: {'apple': 6, 'banana': 10, 'cherry': 4}



# MATCH CASE 
"""It is similar to switch statements in other languages but much more powerful, 
allowing complex patterns like matching data structures and extracting values
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case (matches anything)
"""
def get_day_type(day: str) -> str:
    match day:
        case "Saturday" | "Sunday": # we can give multiple values like this or we can use tuples
            return "Weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case _:
            return "Invalid day"

print(get_day_type("Monday"))  # Output: Weekday
print(get_day_type("Saturday"))  # Output: Weekend
print(get_day_type("Funday"))  # Output: Invalid day

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound


def animal_sound(animal):
    match animal:
        case Animal(species="Dog", sound="Bark"):
            return "This is a Dog, and it barks."
        case Animal(species="Cat", sound="Meow"):
            return "This is a Cat, and it meows."
        case _:
            return "Unknown animal."

dog = Animal("Dog", "Bark")
cat = Animal("Cat", "Meow")
print(animal_sound(dog))  # Output: This is a Dog, and it barks.
print(animal_sound(cat))  # Output: This is a Cat, and it meows.
