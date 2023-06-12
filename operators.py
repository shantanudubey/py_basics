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

print("\nPower of 2 :",2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15, 2**16) #power f operator
power_string = "Poweful powers of 2 :\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(2**4, 2**8, 2**16, 2**32, 2**64, 2**128, 2**256)
print(power_string)



#TBR 

# Operator Precedence :	PE(M&D)(A&S)

print("I will now count my chickens.")
print("Hens		:	", 20 + 30 / 6)			#= 25 + (30/6)
#* and % are calculated in one go from left to right : 100 - 75 % 4 = 100 - 3
print("Roosters	:	", float(100 - 25 * 3 % 4))

print("Now I'll count the eggs.")
print(float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6))	#PE(M&D)(A&S)

print("Is it true that 3 + 2 < 5 - 7 ?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2 ?")
print(float(3 + 2))
print("Whate is  5 - 7 ?")
print(float(5 - 7))
print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater ? ", 5 > -2)
print("Is it greater or equal ? ", 5 >= -2)
print("Is it less or equal ? ", 5 <= -2)
