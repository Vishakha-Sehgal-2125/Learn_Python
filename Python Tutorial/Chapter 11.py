# Loop statements 
""" 
1. While loop - The block of code keeps executing until the condition is true
In while loop the condition is checked first if it is true then the body of loop is executed otherwise not.
If the loop is entered the process of checking condition and executing code is continued until the condition becomes false.
"""
# Syntax:-
"""
start condition
while(condition):
    block of code
    increment/decrement
"""
i = 1 
j = 1
while(i<6):
    print(i)
    i +=1
print("End of program 1")
while(j<6):
    j +=1
    print(j)
print("End of program 2")

list=[10,20,"Thirty",40,50]
ind=0
while(ind<len(list)):
     print(list[ind])
     ind +=1
print("End of program 3") 

"""
2. For loop - for loop is used to iterate through a sequence like list tuple or string
There is a range function in python which is used to generate a sequence of numbers
we can also specify the start stop and step size or skip size as follows
range(start,stop,step_size)
"""
# Syntax :-
"""
for variable in iterable:
    Block of Code
Here, iterable can be a list, tuple, string, range, or any iterable object.
"""
for i in range(1,50,5):
           print(i)

for i in range(5):  # Iterates from 0 to 4
    print("Value:", i)

tuple=(1,2,3,4,5)
for item in tuple:
      print(item)

string="Vishakha"
for s in string:
     print(s)

lists = ["apple", "banana", "cherry"]
for fruit in lists:
    print(fruit)

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

marks = {"Alice": 85, "Bob": 90, "Charlie": 78}
# names= marks.keys()
# scores= marks.values()
for names,scores in marks.items():
     print(f"{names} scored {scores}")

