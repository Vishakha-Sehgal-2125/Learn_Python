# EXCEPTION  HANDLING 
"""There are many built-in exceptions which are raised in python when something goes wrong.
Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause.

try:
   # Code which might throw exception
except Exception as e:
     print(e)

When the exception is handled, the code flow continues without program interruption.
We can also specify the exception to catch like below:

try:
    # Code
except ZeroDivisionError:
    # Code
except TypeError:
    # Code
except:
    # Code          # All other exceptions are handled here.
"""
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful!")
finally:
    print("Execution completed.")

# Output:
# Error: division by zero
# Execution completed.

try:
    value = int("abc")  # Raises a ValueError
    result = 10 / value
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print("All operations were successful!")
finally:
    print("Done handling exceptions.")

# Output:
# ValueError: invalid literal for int() with base 10: 'abc'
# Done handling exceptions.

"""
Key Keywords
try: Block where the code that might cause an exception is placed.
except: Block that handles the exception.
else: Executes only if no exception occurs / try was successful (optional).
finally: Always executes (cleanup actions like closing files, releasing resources).
"""

# raising error
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

if(b==0):
    raise ZeroDivisionError("Cant divide by zero")
else:
    print(a/b)