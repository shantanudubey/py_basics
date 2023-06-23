# All things print()


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
#resetting the behaviour
print()

# Some weird stuff with print() end character mods: 
print("testing", end = '\r\n')
#print("\n\rtest")
#print('\r')
print("again")
print("again", "and", "again", sep = ' - ')

print("-" * 79)