# File Handling 
"""File handling refers to reading or writing data from files. 
Python provides some functions that allow us to manipulate data in the files.
"""
f = open("file.txt", "r") # open() function :- var_name = open("file name", " mode")
""" it opens a file. yaha pr read krna he to "r" likhne ki jarurat nhi 
vo default he baki kuch mode he to mode likhna padega.
"""
data = f.read() # read () function
"""
The read functions contains different methods, read(),readline() and readlines()
read() #return one big string
readlines() #returns a list
readline #returns one line at a time
"""
print(data)
f.close() # close() function :- var_name.close()

string="-said by AJbhairav" # This will not update or add the file.txt but will replace it with this
f1 = open("file.txt","w")
f1.write(string)
f1.close()

string2="Life is too short for ego games\n Just let them win and walk away\n -said by AJbhairav" # This will not update or add the file.txt but will replace it with this
f2 = open("file.txt","w")
f2.write(string2)
f2.close()

# Readin techniques
f3 = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4 =="") # it print lines until there is no line i.e. ""

line = f3.readline()
while(line != ""):
    print(line)
    line = f3.readline()
f3.close()

string4="Hey AjBhairav you are amazing" # This will not update or add the file.txt but will replace it with this
f4 = open("file.txt","a")
f4.write(string4)
f4.close()

# With Statement 
""" Whenever we open the file we need to close it but instead of 
repeatedly closing the file we use with statement.
"""
f = open("file.txt")
print(f.read())
f.close()
# The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())
# You dont have to explicitly close the file

# Modes 
"""
r - to read the content from file
w - to write the content into file
a - to append the existing content into file
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.
"""