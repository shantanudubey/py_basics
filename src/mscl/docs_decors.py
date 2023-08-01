# Documentation Strings and Decorators
import time


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
def decor_spl(func):
    def wrapper():
        print('*'*79)        
        func()
        print('~'*79)
        
    return wrapper

def display():
    print("I stand decorated.")

def show():
    print("Nothing great, me too.")

display = decor_spl(display)
display()
show = decor_spl(show)
show()

# The above is confusing so we can use decorator-tags for the same
def decor_sim(func):
    def wrapper():
        print('-'*79)        
        func()
        print('-'*79)
        
    return wrapper

@decor_sim
def display():
    print("I stand decorated.")

@decor_sim
def show():
    print("Nothing great, me too.")

# Calling is simplified now
display()
show()


# Decorators with arguments : 
def timer(func):
    def calculate(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        print(f"Finished {func.__name__!r} in {runtime:8f} seconds.")
        return value
    return calculate

@timer
def product(num):
    fact = 1
    for i in range(num):
        fact = fact * i + 1
    return fact

@timer
def product_sum(num):
    p = 1
    for i in range(num):
        p = p * i + 1
    
    s = 0
    for i in range(num):
        s = s + i + 1

    return (p, s)

@timer
def time_pass(num):
    for i in range(num):
        i += 1


p = product(10)
print("product  :", p)
p = product(20)
print("product  :", p)
fs = product_sum(10)
print("prod-sum :", fs)
fs = product_sum(20)
print("prod-sum :", fs)
time_pass(20)

print('-'*79)