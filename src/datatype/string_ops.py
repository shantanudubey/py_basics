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

""" Multi line comments : 
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
print(target_string.split()[9])
print('-' * 79)

# Ref : https://docs.python.org/3.11/tutorial/introduction.html
multi_string = """  This is s multi line string,
    To test out the standard behaviour,
    \rand some playing around too.
"""
print(multi_string)
# A better way to do it
multi_string = "This is s multi line string, "\
    "to test out the standard behaviour "\
    "and some playing around too."
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
# Interesting : The default values make sure that str_literals[:i] + str_literals[i:] is always equal to str_literals
print(str_literals[:2] + str_literals[2:])
# Graceful handling of out of range index
print(str_literals[289:8] + str_literals[2:239])
print(len(str_literals))
print('I have eaten ' + str(99) + ' burritos.')

# joins each elemnt of the target string with source except last
str_join = '-'+chr(1)+'-'
print("join     :", str_join.join(str_literals))
print("chr      :", str_join[1])
print("ord      :", ord(str_join[1]))
print('-' * 80)

# Raw string : 
str_raw = r"This is a 'raw' string. \ and ' don't need to be escaped."
print("Raw string       :", str_raw)
print("substring exists :", "raw" in str_raw)

""" - min() : will return the lowest unicode value in the string
    - max() : will return the highest unicode value in the string 
    - ord() : returns the unicode value
    - chr() : returns the character from unicode value
"""
str_test = "Delta_Alpha"
print("built-ins        :", len(str_test), min(str_test), max(str_test))
print("char values      :", ord('0'), ord('A'), ord('_'), ord('a'), ord('t'))
print("characters       :", chr(48), chr(65), chr(95), chr(97), chr(116), chr(196), chr(1))
print('-' * 80)

msg_01 = "first"
msg_02 = "second"
msg_03 = "first"
test_01 = "451"
test_02 = "45.5"
print(msg_01 + msg_02, msg_01, msg_02)
print("rst" in msg_02, "rst" in msg_01)
print(id(msg_01) == id(msg_03))
print(msg_03.isalpha(), test_01.isnumeric(), test_01.isalnum(), test_01.isdecimal(), test_01.isascii(), test_01.isdigit() )
print(test_02.isnumeric(), test_02.isalnum(), test_02.isdecimal(), test_02.isascii(), test_02.isdigit() )
msg_03 = msg_03.replace("st", " se")
print(msg_03)
print('-' * 80)


# LUP : Exercises
s = "Bamboozled"
print(s[0:len(s)-1:2])
s = "   Bamboo zled    "
s = s.lstrip()
s = s.rstrip()
#s = s.strip()
s = s.replace(' ', '')
print(s, len(s))

s = "The Terrible Tiger Tore The Towel."
print(s)
pos = s.find('T', 0)
print(pos, s[pos])
c = s.count('T')
s = s.replace('T', 't', c)
print(s)

s = "Light travels faster than sound. This is why some people appear bright until you hear them speak."
print(s)
s = s.replace("Light", "LIGHT", 1)
s = s.replace("sound", "SOUND", 1)
print(s)

s = "The difference between stupidity and genius is that genius has its limits."
print(s)
res = s.find("genius")
print(res)
res = s.split("genius")
print(res)
res = s.partition("genius")
print(res)

""" 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
    K   E   E   P       Y   O   U   R   S   E   L   F       W   A   R   M
    -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2 -1
"""
s1 = s2 = s3 = "KEEP YOURSELF WARM"
print(id(s1) == id(s2) == id(s3))
print(s1[-0], s1[0], s1[-1], s1[-5])
print("XXXX : ", s1[1:1])
print("Negative indices :", s2[0:3], s2[0:-2], s2[-1:3], s2[:-3], s2[-3:], s2[0:-2])
print('-' * 80)
