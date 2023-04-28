#ex5

name = 'Zed A. Shaw'
age = 35
height = 74
height_cms = round(height * 2.54)
weight = 180
weight_kgs = round(weight / 1.82)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches and {height_cms} cms tall.")
print(f"He's {weight} pounds and {weight_kgs} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depeneding on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")


