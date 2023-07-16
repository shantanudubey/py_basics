# All things print()
import math

print("This is a test line.")
print("We will reserve ('') for characters and (\"\") for strings.")
print('Although it\'s not "illegal".')
print("-" * 79)

# Some peculiar operations related to string operations
# Formatting
emp_name = "Python"
emp_age = 32
emp_code_of_conduct = "PEP-8"
print(f"Greetings! This is {emp_name}, your new colleague. He is {emp_age} years old as of 2023 and has vowed to {emp_code_of_conduct}.")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {} and {}"
print(joke_evaluation.format(hilarious,2))

print("-" * 79)

formatter = "{} {} {} {}"
print("Using the formatter below : ")
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print("-" * 79)

for i in range(5):
	print("count", i, sep=':', end=' ')
# A new print is needed because changing the "end" from the default(new-line) to space retains that for the next print()
# Resetting the behaviour
print()

# Some weird stuff with print() end character mods: 
print("testing", end = '\r\n')
#print("\n\rtest")
#print('\r')
print("again")
print("again", "and", "again", sep = ' - ')
print("-" * 79)

name = "Dummy Name String"
for n in name.split():
	print(f"{n:10}")

# Using format() : older method, better to use f-strings
print("name = {0:25}, salary = {1:8}, bonus = {2:8}".format(name, 92200, 7004))
print("commission = {0:10.2f}".format(29934.58765))

#r, l, b = [int(n) for n in input("Enter r l b : ").split()]
radius, length, breadth = 3, 5, 12
ar_circle = round(math.pi * (radius*radius), 2)
ar_rectangle = length * breadth
print(f"area of circle = {ar_circle} and area of rectangle = {ar_rectangle}")
print("-" * 79)

# Aligned Printing : 
for n in range(1, 10):
	# Left Justified
	print(f"{n:<5}{n**2:<7}{n**3:<8}")

for n in range(1, 20, 2):
	# Right Justified
	print(f"{n:>5}{n**2:>7}{n**3:>8}")
print("-" * 79)

# Left-Center-Right Justifications:
contacts = {
	"Support":1234567890,
	"Service":1324657980,
	"RSA":2345678912
	}

for name, phone in contacts.items():
	print(f"{name:<15}{phone:<10}")

for name, phone in contacts.items():
	print(f"{name:^15}{phone:^10}")

for name, phone in contacts.items():
	print(f"{name:>15}{phone:>10}")

print("-" * 79)

print("Rendezvous", sep='', end=' ')
print()
print(f"{'x =':4}{'14.99':>10}\n{'y = ':4}{'114.39':>10}")
price = 1.5567894
print(f"{price:10.4f}")
print("-" * 79)