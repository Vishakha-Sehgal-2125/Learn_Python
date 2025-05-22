# Functions - 
"""
A group of statements performing a specific task.
A function can be reused by the programmer in a given program anywhere any no. of time
You can pass parameters into a function.
"""
# Syntax
""" def func_name():    - Defining function
        function_logic
    func_name()         - Calling function     
"""
# Types of function
"""
1. Built-in function:- len(),print(),type(),range() etc
2. User defined function:- That user defines in his program
"""
# def add():     #function defination
#         a=int(input("Num1"))
#         b=int(input("Num2"))
#         print(a+b)
# add()          #function call
# without_return=add()
# print(without_return)

# Return Statement
""" The return statement in Python is used to send the result of a function back to the place where it was called. 
When a return statement is executed, the function stops running, and the value provided by return is passed back to the caller.
If no return is used, the function returns None by default
"""
# def add():       #function defination
#         a=int(input("Num1"))
#         b=int(input("Num2"))
#         return(a+b)
# with_return=add()   #function call
# print(with_return)

# Recursion
"""
Recursion is a function which calls itself.
It is used to directly use a mathematical formula as a function.
In maths we write :- factorial(n) = n * factorial(n-1)
Using recursion we can writte it as 
"""
def factorial(n):
        if (n==0 or n==1):
                return 1
        else:
                return n * factorial(n-1)
n = int(input("Enter a Number:"))
print(factorial(n))

"""The Fibonacci sequence is defined as: 
F(n)=F(n-1)+F(n-2) Where: F(0)=0 and F(1)=1 
"""
def fibonacci(n):
    # Base cases: First two numbers of the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Sum of the previous two numbers
    return fibonacci(n - 1) + fibonacci(n - 2)
# Generating the first 10 Fibonacci numbers
for i in range(10):
    print(f"Fibonacci({i}):", fibonacci(i))
