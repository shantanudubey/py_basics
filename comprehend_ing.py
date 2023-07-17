# Comprehensions : List, Set and Dictionary only since they're mutable
import random


print('-'*79)

# Lists using for
lst = [(x, x**2, x**3) for x in range(5)]
print("Lists    :", lst)
lst = [random.randint(10, 100) for n in range(5)]
print("Lists    :", lst)
lst = [int(x) for x in ["10", "20", "30", "40", "50"]]
print("Lists    :", lst)
# Lists using for if
lst = [n for n in range(10, 50) if n % 2 == 0]
print("Lists    :", lst)
lst = [n for n in lst if n >= 20 and n <= 40]
print("Lists    :", lst)




print('-'*79)