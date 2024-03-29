""" Excerpt from #ref : https://www.codingem.com/modulo-in-python/
        To recap, a modulo b in mathematics calculates the remainder in the division between a and b.

        For example, 7 mod 3 represents sharing 7 apples with 3 workers evenly. The result of 7 mod 3 is 1, that is, one apple is going to be leftover.

        In Python, a common way to calculate modulo is using the dedicated modulo operator %.
        Alternatively, if you want to know both the result of the division and the remainder, you can use the built-in divmod() function.
        When doing modular arithmetic with floats, use the math module's fmod() function.
        Modulos also work for negative numbers in Python. However, the way negative modulos are calculated can differ from language to language.

        There are many use cases for modulo in Python. For example, to figure out if a number is odd or even, you need to use modulo.
        Another common use case for modulo is to check if a number is a prime number.
"""

""" Division : 
	N / D = normal division happens and the resulting sign is based on "if both signs sre same then positive else negative"

    Floor Division : 
        N // D = floor(N / D)
            Python uses floor() hence the results are accurate even on the negative side of the number scale.
            JS uses trunc() hence it gives different results for  '//' and also in '%'
            Ref : https://www.codingem.com/modulo-in-python/

    Modulus :
        N % D = N - (D * (N // D)) 
            Or
        N % D = N - (D * floor(N / D))
"""
print('-' * 80)
print("Floor Division (//) operations : ")
print("10 // 3  : ",10 // 3)
print("-10 // 3 : ",-10 // 3)
print("10 // -3 : ",10 // -3)
print("-10 // -3: ",-10 // -3)

print("3 // 10  : ",3 // 10)
print("-3 // 10 : ",-3 // 10)
print("3 // -10 : ",3 // -10)
print("-3 // -10: ",-3 // -10)

print('-' * 80)

print("Modulus (%) operations : ")
print("10 % 3  : ",10 % 3)
print("-10 % 3 : ",-10 % 3)
print("10 % -3 : ",10 % -3)
print("-10 % -3: ",-10 % -3)

print("3 % 10  : ",3 % 10)
print("-3 % 10 : ",-3 % 10)
print("3 % -10 : ",3 %- 10)
print("-3 % -10: ",-3 %- 10)

print('-' * 80)
# Precendence checks
print("3*4 % 5-6 : ", 3 * 4 % 5 - 6)
print("3%4 * 5-6 : ", 3 % 4 * 5 - 6)
print('-' * 80)

# More tests
print("Test :", 2**6 // 8%2)
print("Test :", 9**2 // 5-3, 2 % 3)
print("Test :", 10 + 6 - 2%3 + 7 - 2)
print("Test :", 5 % 10 + 10 - 23 * 4 // 3)
print("Test :", 5 + 5 // 5 - 5 * 5**5 % 5)
print("Test :", 7 % 7 + 7 // 7 - 7 * 7)
print('-' * 80)