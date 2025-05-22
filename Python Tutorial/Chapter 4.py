# String is a data type in python. It is a sequence of characters enclosed in quotes.
a='Vishakha'
b="loves"
C=''' Python'''
# String has a concept of indexing. If we start from left to right we do positive indexing like 0,1,2,... and when we go from right to left we do negetive indexing -n,-(n-1),-(n-2)...
# The index in a string starts from 0 to (length - 1)

length= len(a) # len() function finds the length of string.
print(length)
print(len(a))

# Slicing
# sliced_str = name [ind_start:ind_end]  ---> This is syntax to slice a string.
# here starting index is including and ending index is excluded.
name = a

# Positive Slicing 
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# Negetive Slicing
print(name[-7: -2]) # we convert negetive slicing to positive by writing correspond no. which adds up to length of string (regardless of sign)  
print(name[1:6])

# Incomplete Slicing
print(name[:4]) # is same as print(name[0:4])
print(name[0:4])
print(name[5:]) # is same as print(name[1:8])
print(name[5:8])

# Slicing with Skip values
# sliced_str = name [ind_start:ind_end:skip_value]  ---> This is syntax to slice a string using skip value which indicate how many values to skip.
print(name[1:7:2])
print(name[0:5:3])

# Escape Sequence Characters - Sequence of characters after \

print("Hello\nWorld!") # \n -> inserts a new line

print("Name\tAge\tCity\nAlice\t23\tNew York") # \t -> inserts a tab space 

print("This is a backslash: \\") # \\ ->  prints a single backslash

print('It\'s a sunny day.') # \' -> allows you to use a single quote inside single-quoted strings

print("He said, \"Python is fun!\"") # \" -> allows you to use double quotes inside double-quoted strings


# f-string (formatted string literal) : Syntax -> (f"Your string {expression}")
# It allows you to directly place variables or expressions within curly braces {} in a string, making string formatting much easier and more efficient.
name = "Vishakha"
age = 22
print(f"My name is {name} and I am {age} years young.")
#The f before the string tells Python to treat the string as a formatted string.

length = 5
width = 10
print(f"The area of the rectangle is {length * width}.")

pi = 3.14159265358979
print(f"Pi rounded to two decimal places: {pi:.3f}")


