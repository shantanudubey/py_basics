# Math functions
import math


print('-' * 80)
x = 1.5737
print("pi           :", math.pi)
print("e            :", math.e)
print("degrees      :", math.degrees(x))
print("sqrt         :", math.sqrt(x))
print("ceil         :", math.ceil(x))
print("floor        :", math.floor(x))
print("trunc        :", math.trunc(x))
print("modf         :", math.modf(x))
print("fabs         :", math.fabs(x))
print("exp          :", math.exp(x))
print("log          :", math.log(x))
print("log10        :", math.log10(x))
x = math.ceil(x) + 4
print("factorial    :", math.factorial(x))
print('-' * 80)

""" Trigonometric functions : 
    Ref : 
        - https://www.cuemath.com/trigonometry/trigonometric-table/
        - https://www.mathsisfun.com/sine-cosine-tangent.html
"""
print("sin  :", math.sin(0), math.sin(30), math.sin(45), math.sin(90), math.sin(180), math.sin(270), math.sin(360))
print("cos  :", math.cos(0), math.cos(30), math.cos(45), math.cos(90), math.cos(180), math.cos(270), math.cos(360))
print("tan  :", math.tan(0), math.tan(30), math.tan(45), math.tan(90), math.tan(180), math.tan(270), math.tan(360))
print('-' * 80)

""" Convert degree to fahreheit :
        - celsius = (fahrenheit-32)*5) / 9
        - fahrenheit = (celsius*9/5) + 32
"""
temp_fahrenheit = 100
temp_celsius = ((temp_fahrenheit-32)*5) / 9
print(f"{temp_fahrenheit} fahreheit :", temp_celsius, "celsius")
temp_celsius = 0
temp_fahrenheit = (temp_celsius*9/5) + 32
print(f"{temp_celsius} celsius :", temp_fahrenheit, "fahreheit")
print('-' * 80)

# Some more tests : 
clx_01 = 2 + 3j
print("complex  :", clx_01.real, clx_01.imag, clx_01.conjugate())
print("int      :", int(0b1100001110), str(4.33), 29 // 5, 29 % 5, hex(34567), round(45.6782, 2), math.ceil(3.556), math.ceil(16.7844), 3.45 % 1.22)

print('-' * 80)