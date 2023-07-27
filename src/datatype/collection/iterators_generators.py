# Iterators and Generators
import sys
import random

print('-'*79)
# zip()
words = ["A", "coddle", "called", "Molly"]
numbers = [10, 20, 30, 40, 50]

it = zip(words, numbers)
print("zip  :", it, type(it))

#print("zip  :", *zp)   # *zp unpacks zp so the for loop doesn't execute
for ele in it:
    print("ele  :", ele,  ele[0], ele[1])

# Iteration happens using the public iter() and next() which are 
#   internally referencing __iter__() and __next__() functions of the iterator
#   Once iterated, the object has to be attained afresh to re-iterate
it = zip(words, numbers)
lst = list(it)

# checking for attributes
# list and string is an iterable so has __iter__() but not __next__() since it isn't an iterator yet
s = "Dummy String"
print("iter :", hasattr(s, "__iter__"), hasattr(s, "__next__"))
print("iter :", hasattr(lst, "__iter__"), hasattr(lst, "__next__"))
lst = [1, 2, 3, 4, 5, 6]
lst = iter(lst)
s = iter(s)
# now they've been converted to iterators
print("iter :", s, lst)
print("iter :", hasattr(s, "__iter__"), hasattr(s, "__next__"))
print("iter :", hasattr(lst, "__iter__"), hasattr(lst, "__next__"))

# for-loop works on an interable by converting it to an iterator
#    and using the len(), iter() and next() functions.
s = "Inner Workings"
for ch in s:
    print(ch, end='')
print()

# We can do the same without the for loop
s = iter(s)
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print(next(s), end='')
print()

# This won't print anything as the pointer is now at the last element of s.
#    s has to be re-initialized
for ch in s:
    print(ch, end='')
print()
print('-'*79)

# Generators : functions that create iterators and yield of return
#   yield remembers the last state between calls so call to __next__() works
#   providing a "resume" instead of "restart" behaviour
def gen_avg(data):
    for i in range(0, len(data) - 1):
        yield (data[i] + data[i+1]) / 2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gr = gen_avg(lst)
print("genr :", gr, *gr)
# Since the generator has been unpakced, the pointer is at the last element,
#   next() will raise an Exception. We need to call re-generate
#   If we didn't unpack then the re-generation wasn't needed.
gr = gen_avg(lst)
print("genr :", end=' ')
for i in gr:
    print(i, end=' ')
print()

# Generator Expressions : compact in-line generators, without yield
#   Similar to contaniner comprehensions but use : ()
print("genr :", sum(n**3 for n in range(20)))
print("genr :", max(random.randint(10, 100) for n in range(20)))


# Memory Usage : generators use less memory than a list comprehension
#   as the next element is generated on demand rather than all at once
#   like in lists or other containers
limit = 25568  # Caution : putting in huge values will cause system memory to spike
lst = [n * n for n in range(limit)]
gen = (n * n for n in range(limit))
print("genr :", sys.getsizeof(lst), sys.getsizeof(gen))


# Exercises : 



print('-'*79)