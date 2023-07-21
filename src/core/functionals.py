# Functions
from functools import reduce


print('-' * 79)

def pos_key_demo(a, b, c, d, op="+", msg="hi"):
    print("pos_key_demo : received :", a, b, c, d, op, msg)
    if op == "+":
        print("pos_key_demo :", msg)
        return a + b + c + d
    else:
        return None
    
def test_args(a, b, *args):
    # args is received as a tuple of values
    print("test_args    :", a, b, args)
    print("test_args    :", *args)
    #for i in args:
    #    print(i)

def test_kwargs(a, b, **kwargs):
    # args is received as a dictionary of values
    print("test_args    :", a, b, kwargs)
    print("test_args    :", *kwargs)
    #for k,v in kwargs.items():
    #    print(k, ":", v)

print("func         :", pos_key_demo(100, 200, d=10, c=20))
print("func         :", test_args(11, 22, 99, 999, 9999))
print("func         :", test_kwargs(b=22, a=11, x=99, y=999, z=9999))

# Calling using unpacked collections:
print("func         :", test_args(11, 22, *(99, 999, 9999)))
print("func         :", test_kwargs(b=22, a=11, **{'x':99, 'y':999, 'z':9999}))

print('-' * 79)

# Definition Sequence when all types are expected : 
def print_it(i, j, *args, x, y, **kwargs):
    print(i,j, args, x, y, kwargs)
    print(i,j, *args, x, y, *kwargs)

print_it(10, 20, x=30, y=40)
print_it(10, 20, 99, 999, x=30, y=40, a=11, b=22, c=33)
print('-' * 79)

# Recursion : 
def refact(n):
    if n == 0:
        return 1
    else:
        p = n * refact(n-1)
    return p

print("refact       :", refact(0), refact(1), refact(2), refact(3), refact(4), refact(5), refact(6), refact(7), refact(8), refact(9), refact(10))
print('-' * 79)


# Lambda Functions : anonymous, inline, short functions built at execution time
print("lambda       :", (lambda l: sum(l)/len(l))([1, 2, 3, 4, 5, 6]))

# Higher Order Functions : can receive other functions as arguments or return them
#   e.g. sorted(), map(), filter(), reduce()

d1 = {"oil":230, "clip":150, "stud":175, "nut":35}
print("lambda       :", d1)
# sort by value/count
d1 = sorted(d1.items(), key=lambda kv:kv[1])
print("sorted       :", d1)

# map() : applies a function to each element in the sequence
#    and returns a new sequence containing the result
def func_sqrd(n):
    return n**2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(map(func_sqrd, lst))
print("map          :", l)
# Using lambda
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l = list(map(lambda n1,n2:n1 + n2, lst1, lst2))
print("map          :", l)

# filter() : applies a function to each element of a sequence
#    and returns a new sequence of elements which produce a True result
def is_alpha(n):
    return str(n).isalpha()

lst = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
l = list(filter(is_alpha, lst))
print("filter       :", l)
# Using lambda
l = list(filter(lambda n:str(n).isalpha(), lst))
print("filter       :", l)

# functools.reduce() : performs a rolling computation to sequential pairs of values
#    and returns the result
def get_sum(x, y):
    return x + y

def get_prod(x, y):
    return x * y

lst = [1, 2, 3, 4, 5]
s = reduce(get_sum, lst)
print("reduce       :", s)
p = reduce(get_prod, lst)
print("reduce       :", p)
# Using lambda
sl = reduce(lambda x,y: x + y, lst)
print("reduce       :", sl)
pl = reduce(lambda x,y: x * y, lst)
print("reduce       :", pl)
print('-' * 79)

print('-' * 79)