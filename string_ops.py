# String operations
# Initial inputs from lpthw
# Ref :	https://docs.python.org/3.11/tutorial/introduction.html


print('-' * 79)
# Inserting variables in a string : use the 'f' prefix before the target string
num_types = 2
str_work = "work"
str_no_work = "don't"
str_stmt_1 = f"There are {num_types} types of people."
str_stmt_2 = f"Those who {str_work} and those who {str_no_work}."
# Concatenating 2 strings into one
str_statement = str_stmt_1 + " " + str_stmt_2
print("Original :", str_statement)

""" Multi line comments
    print(str_statement.lower())
    print(str_statement.upper())
    print(str_statement.capitalize())
    print(str_statement.swapcase())
"""
# Destroying the statement's case
str_statement = str_statement.swapcase()
print("Swapped Case :", str_statement)

str_statement = str_statement.upper()
print("Uppercase :", str_statement)

str_statement = str_statement.lower()
print("Lower Case :", str_statement)

# Setting things back to order : Capitalized
str_stmt_1 = str_stmt_1.capitalize();
str_stmt_2 = str_stmt_2.capitalize();
#Need to re-assign the statement because strings are pass by value
str_statement = str_stmt_1 + " " + str_stmt_2
print("Capitalized :", str_statement)

print('-' * 79)

# Inserting the values into the target_string using placeholders
car = "car"
bike = "bike"
budget = 4.267548726488
# Empty placeholders
target_string = "I can afford a {} or a {} not exceeding {} lakhs.".format(car, bike, "%.2f"%(budget))
print(target_string)
# Indexed placeholders 
target_string = "I can afford a {2} or a {0} not exceeding {1} lakhs.".format(bike, "%.2f"%(budget), car)
print(target_string)
# Variables 
budget = round(budget,2)
target_string = f"I can afford a {car} or a {bike} not exceeding {budget} lakhs."
print(target_string)
# Using split()
print(target_string.split()[10])

print('-' * 79)

#Ref :	https://docs.python.org/3.11/tutorial/introduction.html
multi_string = """
    This is s multi line string,
    To test out the standard behaviour,
    \rand some playing around too.
"""
print(multi_string)

print('-' * 79)

print("Auto" "-" "Concatenation" " happens" " like" " this" " but" " only" " with" " literals" ".")
str_literals = "literals"
str_variables = "variables"
print("Use '+' for concatenating " + str_literals + " with " + str_variables + " or " + str_variables + " with " + str_variables + '.')

print('-' * 79)

# String indexing/subscripting : there is no 'char', just s string with length 1
print("String indexing using positive and negative indices : ")
# Positive Indexing : left to right
print(str_literals[0], str_literals[1], str_literals[2], str_literals[3], str_literals[4], str_literals[5], str_literals[6], str_literals[7])
# Negative Indexing : right to left -1 being the last, -2 second last and so on
print(str_literals[0], str_literals[-7], str_literals[-6], str_literals[-5], str_literals[-4], str_literals[-3], str_literals[-2], str_literals[-1])

# Extract substring using slicing : [from_index(included):to_Index(excluded)]
print("Extracting substrings from :", str_literals[0:8])	#8 since the last index is excluded
print(str_literals[0:3])
# Default values are 0 for the first index and size of the string for the second index
print(str_literals[:4], str_literals[2:])
print(str_literals[-2:], str_literals[:-3])
# Interesting : The default values make sure that str_literals[:i] + str_literals[i:] is always equal to str_literals:
print(str_literals[:2] + str_literals[2:])
# Graceful handling of out of range index
print(str_literals[289:8]+str_literals[2:239])
print(len(str_literals))
print('I have eaten ' + str(99) + ' burritos.')
