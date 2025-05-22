#Tuples:- round bracket , immutable , any data type 
a = (1,45,342,3424,False, "Rohan", "Shivam")
c = (1,)
print(a)
print(type(a))
print(type(c))

# Tuple methods are all same to lists 
a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

# no = a.count(45)
# print(no)
# i = a.index(3424)
# print(i)
# print(len(a))
# b = (100, 200, 300)
# concatenated = a + b  # Combine two tuples
# print(concatenated)
repeated = a * 2  # Repeat the tuple elements twice
print(repeated)