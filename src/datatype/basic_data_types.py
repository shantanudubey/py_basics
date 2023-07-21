# Basic data types : int, float, string, bool, byte, complex


""" int : 
        - decimal
        - 0b : binary
        - 0o : octal
        - 0x : hexadecimal
"""
print('-' * 80)
num_01 = 246
bin_01 = 0b1011
oct_01 = 0o455
hex_01 = 0xfa6
# The default conversion of numbers in print() is decimal hence the :b/o/x
print(f"int can also be represented as a binary {bin_01:b}, an octal {oct_01:o} or a hexadecimal {hex_01:x}")
print("int :", num_01, " || ", "bin :", bin(num_01), " || ", "oct :", oct(num_01), " || ", "hex :", hex(num_01))
print("int from bin     :", int('1011', 2))
print("int from oct     :", int('341', 8))
print("int from hex     :", int('21', 16))

# float : fractonal(-314.1528) or expenential(3.141528e2) 
float_01 = -314.1528
float_02 = -3.141528e2
print("float            :",float_01, float_02)

# boolean : 
bool_01 = True
print("boolean          :", bool_01)
print("boolops          :", True + True, False + False, True + False, False + True)

# string : 
str_01 = "This is a test string."
print("string           :", str_01)

# complex : represent real and imaginary part
complex_01 = 3 + 2j
print("complex          :",complex_01, complex_01.real, complex_01.imag, 3 * (2+9j))

# bytes : represent binary data
# Represents 3 bytes with hex values a1a456
byte_01 = b'\xa1\xe4\x56'
print("bytes            :", byte_01)
print('-' * 80)

# Check type : 
print("type()           :", type(num_01), type(bin_01), type(oct_01), type(hex_01), type(float_01), type(bool_01), type(str_01), type(complex_01), type(byte_01))
print('-' * 80)

print("Types can be converted the in-built conversion function for each type :", 
      str(345.345), bool(0), bool(345), bool(-23), int(345.345), float("345"), complex(3,2.6), bytes(2))
print('-' * 80)
