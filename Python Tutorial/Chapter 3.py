# input() function allows the user to take input from the keyboard BUT as a string by default so we have to type-cast it according to the type of input we want. 
a = input("Enter number 1: ")
b = input("Enter number 2: ")
print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)
# this will take input values as string

c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))
print("Number c is: ", c)
print("Number d is: ", d) 
print("Sum is ", c + d)
# this will take input values as integer and give desired results 

