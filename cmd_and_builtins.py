import sys
import keyword
import math


print("Hello Python! Now at version : ", sys.version)
print("Commandline info >> argv: ", sys.argv)
print('-' * 79)

# Python help about any function
help(print)
print('-' * 79)

# Some built-in functions
print("abs      :", abs(-123.45))
print("pow      :", pow(3,2))
print("min      :", min(-123.45, 1, 12, -100))
print("max      :", max(-123.45, 1, 12, -100))
print("round    :", round(-123.45))
print("divmod   :", divmod(10, 3))
print('-' * 79)

# Check all available built-in functions
print(dir(__builtins__))
print('-' * 79)

# Check all available functions in the package : math
print(dir(math))
print('-' * 79)
