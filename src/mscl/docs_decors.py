# Documentation Strings and Decorators

print('-'*79)

# docstring : can be used for any module, function, class or method.

def docstring_test():
    """ This is a function to test the doc-string feature of Python3.
        The doc string must be enclosed in triple quotes to be visible.
    """
    print(docstring_test.__doc__)

docstring_test()
print(docstring_test.__doc__)

def add_num(num_1:int, num_2:int):
    """ This function adds two integers and returns the result as another integer.
    
        num_1   : first integer
        num_2   : second integer
        returns : num_1 + num_2    
    """
    return num_1 + num_2

print("add  :", add_num(100, 223))
# The doc-string is also displayed when help() is used in context
help(add_num)
print('-'*79)



# Decorators : decorate/add functionality to an existing function
def my_decorator(func):
    def wrapper():
        print('*'*79)        
        func()
        print('~'*79)
        
    return wrapper

def display():
    print("I stand decorated.")

def show():
    print("Nothing great, me too.")

display = my_decorator(display)
display()
show = my_decorator(show)
show()

# The above is confusing so we can use decorator-tags for the same
def separate_decorator(func):
    def wrapper():
        print('-'*79)        
        func()
        print('-'*79)
        
    return wrapper

@separate_decorator
def display():
    print("I stand decorated.")

@separate_decorator
def show():
    print("Nothing great, me too.")

# Calling is simplified now
display()
show()






print('-'*79)