"""	Bitwise operators : &, |, ~, ^, >>, <<
	#Ref: 
		- https://www.geeksforgeeks.org/python-bitwise-operators/
		- https://realpython.com/python-bitwise-operators/
		
		In Python, bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on each bit or corresponding pair of bits, hence the name bitwise operators. The result is then returned in decimal format.

			- Python bitwise operators work only on integers.
			- The bitwise operators(&, |, ~) are different from logical operators(and, or, not) as they work one bit at a time and used for integers only while the logical operators are typically used on non-integers like expressions evaluating to a boolean value.
"""

"""	Bitwise(&, |, ~) vs Logical(and, or, not) operatos : 
	#Ref : 
		- https://stackoverflow.com/questions/3845018/boolean-operators-vs-bitwise-operators
		- https://www.geeksforgeeks.org/difference-between-and-and-in-python/
		- 

		- bitwise work only on integers, converting their value to binary for calculations while logical operators work on value of operands to generate a boolean value
		- bitwise isn't lazy evaluated whereas logical is. 
			Short-Circuit / Lazy Evaluation : if the first operand is False/True( and, or respectively) then the second isn't evaluated as the result is the value of the left operand.
		- precedence of bitwise operators is higher

"""

#use bin() to get the binary value of a number
test_num = 24567
print(f"Binary value of {test_num} : ", bin(test_num))
#use (int_val).bit_length() to get the bit length of any integer. Without a pair of parentheses around the number, it would be treated as a floating-point literal with a decimal point.
print(f"Bit length of {test_num} : ", (test_num).bit_length())


"""	In computers we usually represent numbers using 32 bits.
	So binary representation of 10 is (....0000 1010)[32 bits].
	But for ease we take 4 or 8 bits in our calculations
	So, 10 is represented as : 0000 1010 or just 1010 

	a = 10 = 1010 (Binary)
	b = 4 =  0100 (Binary)
"""
a = 10
b  = 4
print(f"Binary of {a}	:", bin(a))
print(f"Binary of {b}	:", bin(b))


"""	Bitwise OR operator Returns 1 if either of the bit is 1 else 0.
	It's a union of a & b.
	a | b = 1010
			|
			0100
		= 1110
		= 14 (Decimal)
"""
print(a, " | ", b, " = ", a | b)

"""	Bitwise AND operator Returns 1 if both the bits are 1 else 0.
	It's an intersection of a & b.
	a & b = 1010
			&
			0100
		= 0000
		= 0 (Decimal)
"""
print(a, " & ", b, " = ", a & b)


"""	Bitwise not operator: Returns ones complement of the number.
	a = 10 = 1010 (Binary)
		~a = 0000 1010
"""
print(f"~{a} = ", ~a)
print(f"~{b} = ", ~b)


"""	Bitwise XOR operator : ^
	Returns 1 if one of the bits is 1 and the other is 0 else returns false.
	It doesn't have a logical counterpart in Python
"""



