#special operations
#Ref : https://www.codingem.com/modulo-in-python/
"""
Division : 
	N / D = normal division happens and the resulting sign is based on "if both signs sre same then positive else negative"

Floor Division : 
	N // D = floor(N / D)
			#Python uses floor() hence the results are accurate even on the negative side of the number scale. JS uses trunc() hence it gives different results for  '//' and also in '%'
		Ref : https://www.codingem.com/modulo-in-python/

Modulus :
	N % D = N - (D * (N // D)) 
		Or
	N % D = N - (D * floor(N / D))
"""

print("\nModulus (%) operations : ")
print("10 % 3  : ",10 % 3)
print("-10 % 3 : ",-10 % 3)
print("10 % -3 : ",10 % -3)
print("-10 % -3: ",-10 % -3)

print("3 % 10  : ",3 % 10)
print("-3 % 10 : ",-3 % 10)
print("3 % -10 : ",3 %- 10)
print("-3 % -10: ",-3 %- 10)

print("\nFloor Division (//) operations : ")
print("10 // 3  : ",10 // 3)
print("-10 // 3 : ",-10 // 3)
print("10 // -3 : ",10 // -3)
print("-10 // -3: ",-10 // -3)

print("3 // 10  : ",3 // 10)
print("-3 // 10 : ",-3 // 10)
print("3 // -10 : ",3 // -10)
print("-3 // -10: ",-3 // -10)

