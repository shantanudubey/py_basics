
# Namespaces : globals() locals()


print('-'*79)

def test():
    x = 99
    global y
    y = 999
    print("test     :", x, y)


x = 10
y = 20
print("names    :", x, y)
test()
print("names    :", x, y)
print("globals():", globals()['x'], globals()['y'])
print("locals() :", locals()['x'], locals()['y'])
print('-'*79)

# Scoping follows LEGB Rule : Local < Enclosing < Global < Built-in

print('-'*79)