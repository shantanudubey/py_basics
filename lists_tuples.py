# Lists : also knows as dynamic arrays, are similar to strings but mutable.
import collections
import operator


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
print("Nested   :", list_2D)
print("Nested   :", list_2D[0][1])
# Unpacking a list in another list using * 
list_unpacked = [*list_char, *list_num]
print("Unpacked :", list_unpacked)
print('-'*79)

# Higher order functions

""" Ref : https://docs.python.org/3/library/functions.html#filter    
    filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) 
        if function is not None and (item for item in iterable if item) if function is None.    
"""

list_demo_01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_demo_02 = [0, 2, 4, 6, 8, 10]

# any() all()
print("any() all()      :", any(list_demo_02), all(list_demo_02))
print("any() all()      :", list_demo_02, id(list_demo_02))

# list.reverse() : modifies the list
list_demo_02.reverse()
print("list.reverse()   :", list_demo_02, id(list_demo_02))
# list.sort() : modifies the list
list_demo_02.sort()
print("list.sort()      :", list_demo_02, id(list_demo_02))

# reversed() : returns a new list
list_demo_02 = list(reversed(list_demo_02))
print("reversed()       :", list_demo_02, id(list_demo_02))
# sorted() : returns a new list
list_demo_02 = sorted(list_demo_02)
print("sorted()         :", list_demo_02, id(list_demo_02))
# Sliced Reversal
list_demo_02 = list_demo_02[::-1]
print("sliced reversal  :", list_demo_02, id(list_demo_02))

print('-'*79)

# CRUD ops
list_demo_02 = [0, 2, 4, 6, 8, 10]
print("Create   :", list_demo_02, id(list_demo_02))
print("Retrieve :", list_demo_02[3], list_demo_02, id(list_demo_02))
list_demo_02.append("XRX")
list_demo_02.append("ABC")
list_demo_02.append(99)
print("Insert   :", list_demo_02, id(list_demo_02))
list_demo_02[list_demo_02.index(99)] = 9999
print("Update   :", list_demo_02, id(list_demo_02))
del(list_demo_02[len(list_demo_02) - 1])
print("Delete   :", list_demo_02, id(list_demo_02))
list_demo_02.remove("ABC")
print("Delete   :", list_demo_02, id(list_demo_02))
list_demo_02.pop()
print("Delete   :", list_demo_02, id(list_demo_02))
print('-'*79)

# Using the deque class to implement a FIFO Queue data structure
# List is not efficient for this as deletion from beginning of list is expensive
q = collections.deque()
q.append("Jimny")
q.append("Brezza")
q.append("Baleno")
q.append("Fronx")
q.appendleft("Alto")
print("deque()  :", q)

print("deque()  :", "pop        :", q.pop())
print("deque()  :", q)
print("deque()  :", "popleft    :", q.popleft())
print("deque()  :", q)
print('-'*79)


# Tuple : An immutable List so CRUD operations are invalid
tpl_01 = ()
print("tuple    :", type(tpl_01))
# Here , is needed othwewise (10) would be considered an int
tpl_01 = (10,)
print("tuple    :", type((10,)), type(10))

# Tuple itself is immutable but the items inside it can change
tpl_01 = ("tuple item", [320, 330], ['a', 'b', 'c'], 99, True)
print("tuple    :", tpl_01)
#tpl_01[1] = ["This is not possible since tuple is immutable."]
# But this is possible
tpl_01[1][0] = 737
tpl_01[1][1] = 777
tpl_01[2][0] = 'Z'
tpl_01[2][1] = 'Y'
tpl_01[2][2] = 'X'
#tpl_01[len(tpl_01) - 1] = False    # invalid since tuple is immutable
print("tuple    :", tpl_01)

# Sorting : using the built-in sorted()
tpl_01 = ([1092, 734, 'a'],[200, 'z'])
#tpl_01 = (23, 45, 11, 8, 3, 999)
print("tuple    :", tpl_01, type(tpl_01))
# sorted() returns a list 
tpl_01 = sorted(tpl_01)
print("tuple    :", tpl_01, type(tpl_01))

# Sorts the below tuple based on price
tpl_01 = (["Jimny", 1500, 1500000], ["Thar", 2000, 1800000], ["Gurkha", 2600, 1700000])
print("tuple    :", sorted(tpl_01, key=operator.itemgetter(2)))

# Unpacking tuple into variables : 
tpl_01 = (10, 20, 30, 40, 50, 60)
print("unpack    :", tpl_01)
a, b, c, d, e, f = tpl_01
print("unpack    :", a, b, c, d, e, f)

# _ : disposable variable : value gets overwritten on each assignment hence the last value is retained
x, _, _, _, _, y = tpl_01
print("unpack    :", x, y, _)

# *_ : single disposable variable
i, *_, j = tpl_01
print("unpack    :", i, j, _)




print('-'*79)