# Objects and Memory Addresses


# Objects don't have names hence are referenced by their memory addresses
print('-' * 79)
num_1 = 220
str_1 = "Test"
print("Object Id    :", id(num_1), id(str_1))
print("type         :", type(num_1), type(str_1))
print("isinstance   :", isinstance(num_1, int), isinstance(str_1, str))

# Assigning 220 to num_2 just pointed num_2 to the address of already instantiated object of class 'int' which is also referenced by num_1
num_2 = 220
print("id           :", id(num_1), id(num_2), num_1 is num_2)
print('-' * 79)


# Swap values of a and b without using a 3rd var or performing any arithmetic
a = 20
b = 10
a, b = b, a
print("Result   :", a, b)
