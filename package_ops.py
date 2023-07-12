import sys
import keyword
# Only import/load sqrt() from the math lib
from math import sqrt
from math import trunc
import random


print("Package : sys")
print("version :", sys.version)
print("platform :", sys.platform)
print("prefix :", sys.prefix)
print("stdout :", sys.stdout)
print("stderr :", sys.stderr)
print("argv :", sys.argv)
print("flags :", sys.flags)
print('-' * 80)

print("Package : keyword")
print("kwlist", keyword.kwlist)
print("softkwlist", keyword.softkwlist)
print('-' * 80)

# Using imported package functions
result = sqrt(225)
print("sqrt :", result)
print('-' * 79)

# Random number between 0 and 100
print("random  :", trunc(random.random() * 100))
print('-' * 79)

# Check all available functions in the package : random
print(dir(random))
print('-' * 79)
