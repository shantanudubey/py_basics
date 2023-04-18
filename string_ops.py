#string operations

print("Testing strings	:")
print('I will now print this : "Quote\'s"', 2, 4, 5)
print("I will now print this : 'Quote\'s'" + "\n")

#inserting variables in a string : use the f prefix before the target string
num_types = 2
str_work = "work"
str_no_work = "don't"
str_stmt_1 = f"There are {num_types} types of people."
str_stmt_1 = f"There are {num_types} types of people."
str_stmt_2 = f"Those who {str_work} and those who {str_no_work}."
str_statement = str_stmt_1 + " " + str_stmt_2	#concatenating 3 strings into one
print(str_statement)

""" Multi line comments
print(str_statement.lower())
print(str_statement.upper())
print(str_statement.capitalize())
print(str_statement.swapcase())
"""
#Destroying the statement's case
str_statement = str_statement.upper()
print(str_statement)

str_statement = str_statement.swapcase()
print(str_statement)

str_statement = str_statement.lower()
print(str_statement)

#Setting things back to order(case)
str_stmt_1 = str_stmt_1.capitalize();
str_stmt_2 = str_stmt_2.capitalize();
print(str_statement)
#Need to re-assign the statement because strings are pass by value
str_statement = str_stmt_1 + " " + str_stmt_2
print(str_statement)

#target_string.format(val1, val2 ...): Insert the formatted values into the target_string
#using placeholders >> empty : {} or indexed : {0} or variables : {var_name}

car = "car"
bike = "bike"
budget = 4.267548726488

#1. empty
target_string = "I can afford a {} or a {} not exceeding {} lakhs.".format(car, bike, "%.2f"%(budget))
print(target_string)

#2. index
target_string = "I can afford a {2} or a {0} not exceeding {1} lakhs.".format(bike, "%.2f"%(budget), car)
print(target_string)

#3. variables
budget = round(budget,2)
target_string = f"I can afford a {car} or a {bike} not exceeding {budget} lakhs."
print(target_string)
#split and extract item at index
print(target_string.split()[10])


