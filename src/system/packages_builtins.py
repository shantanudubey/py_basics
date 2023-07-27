import sys
import keyword
import math
import random


print("Package  : sys")
print("version  :", sys.version)
print("platform :", sys.platform)
print("prefix   :", sys.prefix)
print("stdout   :", sys.stdout)
print("stderr   :", sys.stderr)
print("argv     :", sys.argv)
print("flags    :", sys.flags)
print("path     :", sys.path)
print('-' * 80)

print("Package      : keyword")
print("kwlist       :", keyword.kwlist)
print("softkwlist   :", keyword.softkwlist)
print('-' * 80)

# Using imported package functions
result = math.sqrt(225)
print("sqrt :", result)
print('-' * 79)

# Random number between 0 and 100
print("random  :", math.trunc(random.random() * 100))
print('-' * 79)

# Check all available functions in the package : random
print(dir(random))
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
