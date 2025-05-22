# Types of using functions

# Function with arguments
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20) # Calling the function
print("Sum:", result)

def goodDay(name,ending):
      print("GoodDay"+ name , ending)
goodDay("Kuhu", "Kal maggie lana")
goodDay("Vishakha", "Theek he")

# Function with Default Arguments
def add_numbers(a, b=100):
    return a + b

result = add_numbers(10) # Using default arg.
print("Sum:", result)

def goodDay(name,ending="Thanks"):
      print("GoodDay"+ name , ending)
goodDay("Kuhu") # Uses the default arg
goodDay("Vishakha", "Theek he")

# Function Returning Multiple Values
def calculate(a, b):
    return a + b, a * b # we can also take return like this
# Returning both sum and product as a tuple
sum, product = calculate(3, 5)
print("Sum:", sum)
print("Product:", product)

# Function with Variable-Length Arguments (*args)
def sum_numbers(*args):
    # *args allows the function to accept any number of arguments
    total = 0  # Initialize the total sum to 0
    for num in args:  # Iterate through each number in the arguments
        total += num  # Add the number to the total
    return total  # Return the calculated sum
# Calling the function with different numbers of arguments
print("Sum of 1, 2, 3:", sum_numbers(1, 2, 3))
print("Sum of 4, 5, 6, 7, 8:", sum_numbers(4, 5, 6, 7, 8))

def concatenate_strings(*args):
    # *args allows passing multiple strings
    result = ""  # Start with an empty string
    for string in args:  # Iterate over each argument
        result += string + " "  # Append the string with a space
    return result.strip()  # Return the concatenated string, removing extra spaces
# Calling the function with different sets of strings
print(concatenate_strings("Hello", "world!"))  
print(concatenate_strings("Python", "is", "fun")) 

# Function with Keyword Arguments (**kwargs)
"""**kwargs allows a function to accept any number of keyword arguments.
Keyword arguments are passed as key-value pairs (e.g., key=value).
Inside the function, kwargs behaves like a dictionary.
"""
def print_details(**kwargs):
    # **kwargs allows the function to accept any number of keyword arguments
    for key, value in kwargs.items():  # Iterate through the key-value pairs
        print(f"{key}: {value}")  # Print the key and its corresponding value
# Calling the function with keyword arguments
print_details(name="Alice", age=25, country="India")
print_details(brand="Tesla", model="Model S", year=2023)

def greet_user(**kwargs):
    # Use specific keys from the kwargs dictionary
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}!")  # Greet the user by name
    else:
        print("Hello, Guest!")  # Default greeting if name is not provided
# Calling the function with different keyword arguments
greet_user(name="Bob", age=30)
greet_user(country="USA")

# Lambda Function - A user-defined anonymous function using lambda.
"""lambda arguments: expression
Arguments: The input parameters to the lambda function.
Expression: A single-line operation or calculation that the lambda function performs.
"""
square = lambda x: x ** 2
print("Square of 4:", square(4))

add = lambda x, y: x + y
print("Sum:", add(5, 10))  # Output: 15
