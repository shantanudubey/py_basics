# Regular Expressions

import re

print('-' * 80)
test_str = "Regular Expressions"
print("re       :", re.search("xp", test_str))

test_str = "This is dummy sample string for testing regular expressions in Python3 @ 2023"
print("re       :", re.search("[xp]re", test_str), re.search("[re]xp", test_str))
# Blanks can be represented in either way but explicit is preferred " [' ']
print("re       :", re.search("[@][' ']", test_str), re.search("[@][ ]", test_str))
print('-' * 80)

# LUP
# Metacharacters : [], -, ^, |, \, ., 

# Character Class : 
print("Meta []:", re.search("[bh]owl", "howler"))
print("Meta []:", re.search("[bh]owl", "xowler"))
# Range : - 
print("Meta - :", re.search("[a-z]owl", "xowler"))
# Regex for PIN code : Range and Character Class
print("re PIN :", re.search("[0-9][0-9][0-9][0-9][0-9][0-9]", "123456789"))
# Complement : ^
print("Meta ^ :", re.search("[^0-9]", "Zebra"))
print("Meta ^ :", re.search("[0-9]", "Zebra"))
# Alternation : |
print("Meta | :", re.search("[a-z|A-Z|0-9]", "Zebra"))
print("Meta | :", re.search("[a-z|A-Z|0-9]", "1Zebra"))
print("Meta | :", re.search("[a-z|A-Z|0-9]", "zebra"))
print("Meta | :", re.search("[a-z|A-Z|0-9]", "@!#$%^&*()_+"))
# Escape and special character class : \
print("Meta \ :", re.search("[a-z\$]", "$21.99"))
print("Meta \ :", re.search("[a-z?@#]", "?#4567abcd"))
# Special Character Class : \
print("Meta \ :", re.search("\d", "$21.99"))
print("Meta \ :", re.search("\D", "$21.99"))
print("Meta \ :", re.search("\s", "\tRegular Expression"))
print("Meta \ :", re.search("\S", "\tRegular Expression"))
print("Meta \ :", re.search("\w", "USD 21.99"))
print("Meta \ :", re.search("\W", "USD21.99"))
print("Meta \ :", re.search("\W", "RegEx"))
# Anything except newline : . 
print("Meta . :", re.search("[\s.]", "Test "))
print("Meta . :", re.search("[A.Z]", "ANZ"))


# ??? not sure about the significance of single or multiple .
print("Meta . :", re.search("[..Z]", "ANZ"))


print('-' * 80)
# Repetition Qualifiers : 
print("Rep *    :", re.search("\d-*\d", "aa45aa"), re.search("\d-*\d", "aa4---5aa"))
print("Rep +    :", re.search("\d-+\d", "aa4---5aa"))
print("Rep ?    :", re.search("\d-?\d", "a4-5a"), re.search("\d-?\d", "aa4---5aa"))
# Email
print("Email    :", re.search("\w*@gmail.com", "abs123@#!@gmail.com"))
# ??? Check
print("Email    :", re.search("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", "abs.123@fhbfwbgb12.ai345"))
#PIN
print("PIN      :", re.search("[0-9]{6}", "123456"))
#Characters of length
print("Char 6   :", re.search("\w{6}", "ARD456"))
print("Char 6-8 :", re.search("\w{6,8}", "ARD456789"))
print('-' * 80)

# RegEx Anchors : ^ $
print("Anchor ^ :", re.search("^Ram", "Ramrod"))
print("Anchor ^ :", re.search("^Ram", "TenaliRam"))
print("Anchor $ :", re.search("Ram$", "TenaliRam"))
print('-' * 80)

# RegEx Grouping : ()
print("Group    :", re.search("(fun[cd])", "function"), re.search("(fun[ad])", "function"))
print("Group    :", re.search("(fun[cd]+)", "function"), re.search("(fun[cd]+)", "funfundtion"))
print("Group    :", re.search("(fun[c]){1,3}(on)?", "function"))
print('-' * 80)


# Exercises : 
print("rex  :", re.search("\w+", "A"))
print("rex  :", re.search("\d{2}", "12"))
print("rex  :", re.search("\w{1,}", "AS"))
print("rex  :", re.search("\w{2,4}", "ASRDE"))
print("rex  :", re.search("A*B", "ADRXFGB"))
print("rex  :", re.search("\d+", "1XA"))
print('-' * 80)

# Playground : 


#print('-' * 80)