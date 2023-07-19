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

# Lists using for if-else
lst = [n if (n >= 20 and n <= 40) else "OOR" for n in lst]
print("Lists    :", lst)

# Multiple fors and if-else
arr = [[12, 24, 36, 48], [1, 3, 5, 7], [0, 2, 4, 6]]
lst = [j if j < 10 else "OOR"  for i in arr for j in i]
print("Lists    :", lst)

# Nested for : fors are nested not the result
lst = [a + b for a in [1, 3, 7] for b in [0, 2, 6]]
print("Lists    :", lst)

# Nested Comprehension : the result is nested
lst = [[a + b for a in [1, 3, 7]] for b in [0, 2, 6]]
print("Lists    :", lst)
print('-'*79)

# Generate all combinations of 1, 2 and 3
lst = [(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3]]
print("Lists    :", lst)

# Generate all unique combinations of 1, 2 and 3
lst = [(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3] \
       if j != k and i != j and k != i]
print("Lists    :", lst)
print('-'*79)


# Set Comprehension : same as lists, just the brackets differ
# Generate all unique combinations of 1, 2 and 3
s = {(i, j, k) for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3] \
       if j != k and i != j and k != i}
print("Sets     :", lst)
print('-'*79)


# Dictionary Comprehension : 
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}
d1 = {k:v**3 for (k,v) in d.items() if v > 4}
print("Dicts    :", d1)

d2 = {k:("even" if v%2 ==0 else "odd") for (k,v) in d.items()}
print("Dicts    :", d2)
print('-'*79)


# Exercises : 


print('-'*79)