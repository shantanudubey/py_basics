# Control Flows


#x = int(input("Enter a number :"))
#print("You entered :", x)
# Above code disabled for easier testing
x = 22

if x < 0:
	x = 0
	print('Negative value received.')
elif x == 0: 
	print('Zero value received.')
elif x == 1: 
	print('One received.')
else :
	print('Value > 1 received.')
print('-' * 80)


# Interesting Behaviours : 

# Character and String comparisons are done on unicode values
print("Comparisons	:", "Santosh" < "Adi", "Santosh" < "adi")

# and evaluates all expressions and returns the last expression if evaluation is True else returns the first value which evaluates to False
a = 40
b = 30
# Since this evaluates to True the last expression(35) is retunred which gets assigned to x
x = 75 and a >= 20 and b < 60 and 35
# Since this evaluates to False, the first False value is returned which is False in this case and assigned to y
y = -30 and a >= 20 and b < 15 and 35
# Since this evaluates to False, the first False value is returned which is 0 and assigned to z
z = -30 and a >= 20 and 0 and 35
print("and		:", x, y, z)

# or evaluates all expressions and returns the first value that evaluates to True else returns the last value which evaluates to False
a = 40
b = 30
# Since the first expression evaluates to True that is returned(75) and assigned to x
x = 75 or a >= 20 or 60
# Since the first expression evaluates to True that is returned(True) and assigned to y
y = a >= 20 or 75 or 60
# Since the first and second expressions evaluate to False the last expression which evaluates to True is returned(35) and assigned to z
z = a < 20 or 0 or 35
print("or		:", x, y, z)

# 0 is False, any non-zero integer is True including negatives
a = 10
b = 0
c = -10
print("not		:", a, b, c)
a = not b
print("not		:", a, b, c)
print("not		:", b and c, b or c, bool(b and c), bool(b or c))
print('-' * 80)

"""	Conditional Expression : <expression_1> if <condition> else <expression_2> 
		if condition is true then expression_1 is evauated else expression_2 is evaluates
"""
age = 28
status = "adult" if age >= 18 else "minor"
humidity = 81
temp_set = 25 if humidity > 75 else 27
print("conditional	:", status, temp_set)
sunny = True
print("conditional	:", "Let's go to the", "beach" if sunny else "room.")

# Nested Conditionals
wt = 72
msg = "Obese" if wt > 85 else "Hefty" if wt > 60 else "Prim"
print("conditional	:", msg)

# all()		any()
a, b, c = 10, 20, 30
print("all() any()	:", all([a > 5, b > 10, c < 20]), any([a > 5, b > 10, c < 20]))

# Use case : pass
n = 13
if n > 0:
	flag = True
	print("conditional	:", n * n)
elif n < 0:
	flag = False
	print("conditional	:", n)
else:
	# This is a better way to indicate the intention of doing nothing and avoid its mis-interpretation as missing code 
	pass

print('-' * 80)

# Exercises : 
a = 11
b = 20 if a < 10 else 30
print("Exercises	:", b)

x = 3; y = 3.0; print("Exercises	:", "x and y are", "equal" if x == y else "not equal")

i, j, k = 4, -1, 0
w = i or j or k
x = i and j and k
y = i or j and k
z = i and j or k
print("Exercises	:", w, x, y, z)
print("Exercises	:", 30 or 40 or 60 and 0)


print('-' * 80)