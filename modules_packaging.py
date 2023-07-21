# Modules and packages

""" We cannot import packages/modules from above your current working directory.
    Ref : https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python
"""

import src.util.func_utils as fu
from src.util.func_utils import displayModuleName as dmn

from messages.funny.modf3 import funf3
from messages.curt.modc2 import func2



print('-'*79)

def display():
    print("You cannot make History if you use Incognito")


print("Module name :", __name__)
display()

# Using aliased imports
dmn()
fu.show()
fu.display()

# Using packaged modules
funf3()
func2()
print('-'*79)



print('-'*79)