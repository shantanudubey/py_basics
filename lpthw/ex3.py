#ex3
#Operator Precedence :	PE(M&D)(A&S)

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

