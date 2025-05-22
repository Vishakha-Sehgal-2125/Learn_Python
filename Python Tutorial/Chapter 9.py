#Sets :- A set is a collection of multiple values which is both unordered and unindexed. curly brackets. 
s = {} # empty dict not set 
emp_set = set() # this will create an empty set
s =  {1,5,32,56,6,6,6,5,5,"Me"}
print(s,type(s)) #unodered order doesnt matter
# cant change existing elements in set
# s.add(789)
# print(len(s))
# s.remove(5)
# print(s)
# s.remove(100) # gives error 100 doesnt exist
# s.discard(100)  # Doesn't raise an error
# popped_element = s.pop()
# print(popped_element)
# s.clear()
s2 = {10, 20, 56, "Hello"}
union_set = s.union(s2)
print("Union of s and s2:", union_set)
intersection_set = s.intersection(s2)
print("Intersection of s and s2:", intersection_set)
difference_set = s.difference(s2)
print("Difference of s and s2:", difference_set)
print(s.issubset(s2))
print(s.issuperset(s2))
