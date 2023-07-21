# Iterators and Generators


print('-'*79)
# zip()
words = ["A", "coddle", "called", "Molly"]
numbers = [10, 20, 30, 40, 50]

zp = zip(words, numbers)
print("zip  :", zp, type(zp))

#print("zip  :", *zp)   # *zp unpacks zp so the for loop doesn't execute

for ele in zp:
    print("ele  :", ele[0], ele[1])


print('-'*79)