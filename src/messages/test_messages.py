
""" We cannot import packages/modules from above your current working directory.
    Ref : https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python
"""

# Absolute imports
from curt.modc1 import func1
from curt.modc2 import func2
from curt.modc3 import func3
from funny.modf1 import funf1
from funny.modf2 import funf2
from funny.modf3 import funf3

print('-'*79)

funf1()
funf2()
funf3()
func1()
func2()
func3()

print('-'*79)