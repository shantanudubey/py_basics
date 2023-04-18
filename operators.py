#Operator Precedence	:	PE (M&D)(A&S)
#	PE (M&D)(A&S)	:	MD and AS are treated as one unit and processed left to right
#	https://www.tutorialspoint.com/python3/python_basic_operators.htm#
#	https://www.w3schools.com/python/python_operators.asp

print("Testing operators following : PE(M&D)(A&S)")
print("Operators	:	", 100 - 25 % 9 * 4)

print("plus minus	:	", 20-10+50+80-70)

print("div mult	:	", 100/(3*4))
print("div mult	:	", int(100/(3*4)))
print("div mult	:	", float(100/(3*4)))
print("div mult	:	 %.2f" %(100/(3*4)))
print("div mult	:	 %.3f" %(100/3*4))
print("floor div	:	", 100/3*4, 100//3*4)

print("div mult mod	:	", 100/3*4*10%4)
print("div mult mod	:	", int(100/3*4*10%4))
#print("Tests	:	", 100 + 5 * 3, 100//3)

print("div mult mod	:	", 100 + 20 - 10 + 100/3*4*10%4)

