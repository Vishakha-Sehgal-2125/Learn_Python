#Dictonary:- collection of key value pair , mutable , indexed , unordered , cant contain duplicate value
d = {} # Empty dictionary

# <dictionary-name> = {<key>: value, <key>: value ...}
marks = {"Harry": 100,"Shubham": 56,"Rohan": 23}
print(len(marks))
print(marks, type(marks),"Kuhu")
print(marks["Harry"])
print(marks["Shubham"]) # if you need any value from dict. you dont need to put index you can get it from key 
#print(marks[0]) #This cant be done in dict. will give key error 

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Me"          
}
print(marks["Harry"])
print(marks[0])
#print(marks[56]) #This will give error


# print(marks.items()) #- give key value pairs in form of tuples
print(marks.keys()) #- left hand side
print(marks.values()) #- right hand side
# marks.update({"Harry": 99, "Renuka": 100})
# marks["Rajat"]= 200
# print(marks)
# print(marks.get("Harry2")) # Prints None - boolean function
# print(marks["Harry2"]) # Returns an error
# removed_value = marks.pop(0)  # Removes the key `0` and returns its value
# print(removed_value)
# marks.popitem()  # Removes and returns the last key-value pair
print(marks)
print("Harry" in marks)  # Checks if "Harry" is a key in the dictionary
print("Me" in marks)  # Checks if "Me" is a key (note: it's a value here)
# marks.clear()  # Removes all items from the dictionary
print(marks)