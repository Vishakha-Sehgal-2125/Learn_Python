# Python lists -> These are containers to store a set of values of any data type.
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable
print(friends[0])
print(friends[1:4])
friends.append("Kuhu")
print(friends)

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry") # we write element in the bracket 
print(friends)

l1 = [1, 34,62, 2, 6, 11]
print(type(l1))
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(2, 333333) # we write index , element 
# print(l1)
# Insert 333333 such that its index in the list is 3
# value = l1.pop(3) # we write only index 
# print(l1) 
# print(value)
# l1.remove(11) # we write only element
# print(l1)
# l1.clear()
# cnt=l1.count(11)
# print(cnt)
# ind =l1.index(62)
# print(ind)
# print(l1)
l2 = [10,20,30]
print(l1+l2)
print(l2 * 2)