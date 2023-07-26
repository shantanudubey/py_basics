# Iterators and Generators


print('-'*79)
# zip()
words = ["A", "coddle", "called", "Molly"]
numbers = [10, 20, 30, 40, 50]

it = zip(words, numbers)
print("zip  :", it, type(it))

#print("zip  :", *zp)   # *zp unpacks zp so the for loop doesn't execute
for ele in it:
    print("ele  :", ele[0], ele[1])

# Iteration happens using the oublic iter() and next() which are 
#   internally referencing __iter__() and __next__() functions of the iterator
#   Once iterated, the object has to be attained afresh to re-iterate

it = zip(words, numbers)
lst = list(it)

# checking for attributes
s = "Dummy String"
print("iter :", hasattr(s, "__iter__"), hasattr(s, "__next__"))
s = iter(s)
print("iter :", hasattr(s, "__iter__"), hasattr(s, "__next__"))
print("iter :", hasattr(lst, "__iter__"), hasattr(lst, "__next__"))
lst = iter(lst)
print("iter :", hasattr(lst, "__iter__"), hasattr(lst, "__next__"))

 



print('-'*79)