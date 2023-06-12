import sys
import keyword
# Only import/load sqrt() from the math lib
from math import sqrt


print("Hello Python! Now at version : ", sys.version)
print("Commandline info >> argv: ", sys.argv)

print('-' * 79)

# Using imported package functions
result = sqrt(225)
print("sqrt :", result)
print("Keywords :\n", keyword.kwlist)
