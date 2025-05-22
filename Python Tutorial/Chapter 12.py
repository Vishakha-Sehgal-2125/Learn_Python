# Break,Continue and Pass
"""
Break statement instructs a programme to exit the loop right now
"""
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
print("Loop ended")

"""
Continue statement Is used to stop the current iteration of the loop and continue with the next one 
it instructs the programme to it instructs the programme to skip this iteration 
"""
for i in range(10):
    if i == 5:
        continue  # Skip this iteration
    print(i)
print("Loop ended")

"""
Pass statement instructs to do nothing; 
it's a placeholder when a statement is syntactically required but no action is needed.
"""
for i in range(645):
    pass   # for future use # gives error without pass 
i = 0
while(i<5):
    print(i)
    i +=1
    