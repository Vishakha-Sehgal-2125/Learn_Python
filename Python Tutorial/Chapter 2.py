# Variables other name given to a memory location in a programme for example
a=10
b=20
c=a+b
print(c)
print("c")
print(a+b)
print("a+b")
print("a"+"b")
print("Kuhu"+"Khandelwal")
# print(a+"b")   #this gives error because an integer and a string cant be added
print(str(a)+"b")


# Data types define the types of variable that we have used
d = 1  #integer 
e = 5.22  #floating point number
f = "Harry"  #string
g = False  #boolean variable
h = None  #none type variable


# Operators are used to perform operations on variables and values.
i = a + b # +, -, *, /, %, ** , //
print(i) # Arithmetic Operators

j = 4-2 # Assign 4-2 in a
print(j) # Assignment Operators

# j += 3 # pehle increase kro fir assign kro
# j -= 3 # pehle decrease kro fir assign kro

k = 5==5 # Compare krte he and returns Boolean Values
print(d) # Comparison Operators

l = True or False # Logical Operators

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))


# Type-casting is a method to change the data type of a variable. 
# We can check datatype using type() function
r = "31.2"
print(type(r))
print(type(float(r))) #because r is a string and it has to be float.
# t = type(s) 
# print(s)
# print(t)

