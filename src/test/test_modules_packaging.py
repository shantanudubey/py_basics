# Modules and packages

""" Imports should be at the top of the file, after any module comments or docstrings
    Imports should be arranged, in sequence, each category separated by a space : 
        - Builtin
        - Third Party
        - Local Application    
    PEP-8 explicitly recommends absolute imports.
    
    *We cannot import packages/modules from the parent level or above it.
    
    - __init.py file is used to tell python to treat the folder as a package
    
    Ref : 
        - https://realpython.com/absolute-vs-relative-python-imports/        
        - https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python        
        - https://www.lightly-dev.com/blog/importing-from-parent-directory-python/
"""

# Standard library imports
import os
import sys

# Third part imports
# Example : Flask 

# Get OS path for current and parent directories
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
# Get the grand-parent dir also the project root 
project_dir = os.path.dirname(parent_dir)
# Add the parent directory to sys-path
sys.path.append(parent_dir)
# Add the project directory to sys-path as it contains the libs
sys.path.append(project_dir)
print("Current      :", current_dir)
print("Parent       :", parent_dir)
print("Project      :", project_dir)
print("sys.path     :", sys.path)

# Local application imports
import util.func_utils as fu
from util.func_utils import displayModuleName as dmn

from messages.curt.modc1 import func1
import messages.curt.modc2 as mc2
import messages.funny.modf1 as mf1
import messages.funny.modf2 as mf2
import projectlibs.libtest as lt


print('-'*79)
print("OS           :", os.getcwd())
print("OS           :", os.getcwdb())

def display():
    print("You cannot make History if you use Incognito")

print("Module Name  :", __name__)
display()

# Using aliased imports
dmn()
fu.displayModuleName()
fu.show()
fu.display()
print('-'*79)

# Using packaged modules
func1()
mc2.func2()
mf1.funf1()
mf2.funf2()
print('-'*79)

lt.show_message()
lt.test_lib_util()

print('-'*79)