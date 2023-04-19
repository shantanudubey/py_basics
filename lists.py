#lists
#lists are similar to strings but mutable

demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	#assign the reference to the list to demo 
print(demo[0:10], demo[:])
print(demo[2:8])
print(demo[-7:8])
print(demo + [11, 12, 13, 14, 15])

demo.append(1001)
print(demo)
#lists are mutable
demo[10] = 11
print(demo)

demo_1 = demo
demo_1[2:5] = ['A', 'B', 'C']
#same since demo_1 is a shallow copy of demo so in this case effectively its pass by ref
print("#same since demo_1 is a shallow copy of demo so in this case effectively its pass by ref")
print(demo_1, demo)
demo_1 = []	#clear the reference
#demo_1 is now assigned to an empty list instead of demo 
print("#demo_1 is now assigned to an empty list instead of demo")
print(demo_1, demo)
demo_1 = demo
demo = []	#clear the reference
print("#demo is now assigned to an empty list but demo_1 is now assigned to the original list")
print(demo_1, demo)
#now we have lost all references to the original list 
demo_1 = []	#clear the reference
print("#now we have lost all references to the original list and is now irrecoverable")
print(demo_1, demo)

#re-populate the lists 
demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	#assign the reference to the list to demo 
demo_1 = demo	#assign the reference in demo to demo_1 which is the reference to the list
print("Since both variables point to the same reference of the list, demo and demo_1 are equal")
print(demo, demo_1, demo == demo_1)
#now we have gone into each element of the list and changed its value to blank, so both demo and demo_1 are pointing to an empty list
demo[:] = []	#clear the list
print("#now we have gone into each element of the list and changed its value to blank, so both demo and demo_1 are pointing to an empty list and still equal")
print(demo, demo_1, demo == demo_1)
#re-assigning demo to the reference of another list
demo = [1]
#now since demo and demo_1 point to different lists they aren't equal anymore
print("#now since demo and demo_1 point to different lists they aren't equal anymore")
print(demo, demo_1, demo == demo_1)

#Nested lists
list_char = ['a', 'b', 'c', 'd']
list_num = [1, 2, 3, 4]
list_2D = [list_char, list_num]
print(list_2D)
print(list_2D[0][1])
