# Functions

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
print('-' * 79)

# Definition Sequence when all types are expected : 
def print_it(i, j, *args, x, y, **kwargs):
    print(i,j, args, x, y, kwargs)
    print(i,j, *args, x, y, *kwargs)

print_it(10, 20, x=30, y=40)
print_it(10, 20, 99, 999, x=30, y=40, a=11, b=22, c=33)







print('-' * 79)