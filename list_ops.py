# Lists : also knows as dynamic arrays, are similar to strings but mutable.

print('-'*79)
""" 0   1   2   3   4   5   6   7   8   9
    1   2   3   4   5   6   7   8   9   10
    -10  -9  -8  -7  -6  -5  -4  -3  -2 -1
"""
# Assign the reference to the list to demo 
demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(demo[0:10], demo[:])
print(demo[2:8])
print(demo[-7:8])
print(demo + [11, 12, 13, 14, 15])

demo.append(1001)
print(demo)
# Lists are mutable
demo[10] = 11
print(demo)
print('-'*79)

# SHALLOW COPY : 
demo_1 = demo
demo_1[2:5] = ['A', 'B', 'C']
# Same since demo_1 is a SHALLOW COPY of demo so in this case effectively its pass by ref
print("Same since demo_1 is a SHALLOW COPY of demo so in this case effectively its pass by ref.")
print(demo_1, demo)
# Clear the reference
demo_1 = []	
# demo_1 is now assigned to an empty list instead of demo 
print("demo_1 is now assigned to an empty list instead of demo")
print(demo_1, demo)
demo_1 = demo
# Clear the reference
demo = []
print("Demo is now assigned to an empty list but demo_1 is now assigned to the original list.")
print(demo_1, demo)
# Now we have lost all references to the original list 
# Clear the reference
demo_1 = []
print("Now we have lost all references to the original list and is now irrecoverable.")
print(demo_1, demo)

# DEEP COPY : 
print("DEEP COPY avoids this issue by copying the contents of one list to another")
demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
demo_1 = []
# This creates a new list which is a merge of an empty list and contents of demo
demo_1 = demo_1 + demo
print(demo, demo_1, id(demo), id(demo_1), demo is demo_1)
print('-'*79)

# Re-populate the lists 
# Assign the reference to the list to demo 
demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	
# Assign the reference in demo to demo_1 which is the reference to the list
demo_1 = demo	
print("Since both variables point to the same reference of the list, demo and demo_1 are equal.")
print(demo, demo_1, demo is demo_1)
# Now we have gone into each element of the list and changed its value to blank, so both demo and demo_1 are pointing to an empty list
# Clear the list
demo[:] = []	
print("Now we have gone into each element of the list and changed its value to blank, so both demo and demo_1 are pointing to an empty list and still equal.")
print(demo, demo_1, demo is demo_1)
# Re-assigning demo to the reference of another list
demo = [1]
# Now since demo and demo_1 point to different lists they aren't equal anymore
print("Now since demo and demo_1 point to different lists they aren't equal anymore.")
print(demo, demo_1, demo is demo_1)
print('-'*79)

# Nested lists
list_char = ['a', 'b', 'c', 'd']
list_num = [1, 2, 3, 4]
list_2D = [list_char, list_num]
print(list_2D)
print(list_2D[0][1])
print('-'*79)

# Higher order functions

""" Ref : https://docs.python.org/3/library/functions.html#filter    
    filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) 
        if function is not None and (item for item in iterable if item) if function is None.    
"""

list_demo_01 = [1,2,3,4,5,6,7,8,9]
list_demo_02 = [2, 4, 6, 8, 10]


print('-'*79)