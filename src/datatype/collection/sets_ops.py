"""
Sets : unordered mutable container
    - no duplicates since it uses a hashing technique to store elements 
        and since the hash of an element will be same so no duplicates
    - subscripting isn't available so concat, merge, slice won't work
    - can only contain immutable elements (hash value doesn't change)
        , so tuples and strings are ok but list is not
    - mutable so CRUD works but retireve is only for validations and comparisons
    - unpacking works
    - cannot be nested
    - frozenset() : creates an immutable set
    - enumerate() : enumeration is done in access-order not insertion-order
"""
print('-' * 79)

set_01 = {10, 20, 30, 40, 50}
set_02 = {10, 20, 30, 40, 50}
print("set      :", set_01, set_02)
print("set      :", id(set_01), id(set_02))

temp = {"Alpha", "Delta", "Sigma"}
# Unpacking
set_03 = {*set_01, *temp}
print("set      :", set_03)
print('-' * 79)

# CRUD
# Create/Insert
fruits_avail = {"Mango", "Banana", "Guava", "Orange"}
fruits_avail.add("Apple")
fruits_avail.add("Grapes")
fruits_avail.add("Watermelon")
print("Create   :", fruits_avail)
fruits_foreign = {"Kiwi", "Passionfruit", "Dragonfruit", "Blueberry"}
fruits_summer = {"Watermelon", "Grapes", "Orange", "Mango"}
fruits_gen = {"Apple", "Banana", "Guava"}
fruits_spl = {"Jackfruit", "Avocado"}

# Retrieve :
#   doesn't work as subscripting [] isn't supported
#   Use them as a data source for comparison/validation
print("Retrieve :", "Apple" in fruits_avail, "Banana" in fruits_avail
      , fruits_foreign.issubset(fruits_avail), fruits_avail.issuperset(fruits_foreign)
      , fruits_avail.isdisjoint(fruits_foreign))
print("Retrieve :", fruits_summer.issubset(fruits_avail), fruits_avail.issuperset(fruits_summer))

# Update
fruits_avail |= fruits_spl
print("Update      :", fruits_avail)
fruits_avail.update(fruits_foreign)
print("Update      :", fruits_avail)

# Delete
fruits_avail.discard("Not a Fruit")
fruits_avail.discard("Dragonfruit")
fruits_avail.remove("Passionfruit")
print("Delete       :", fruits_avail)
# Delete all
fruits_avail.clear()
print("Delete All   :", fruits_avail)
print('-' * 79)


# Mathematical operations
# Natural numbers start from 1 
naturals = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# Whole numbers start from 0
wholes = naturals.copy()    # Deep copy
wholes.add(0)
evens = {0, 2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9, 11}
print("maths            :", wholes, naturals)
print("union |          :", evens | odds)
print("intersection &   :", evens & odds, naturals & evens, naturals & odds)
print("difference -     :", evens - odds, odds - naturals, naturals - odds, naturals - evens)
print("symmetric diff ^ :", evens ^ odds, odds ^ naturals, naturals ^ odds, naturals ^ evens)
print("comparison       :", naturals > evens, wholes > evens, naturals > odds, naturals < wholes)
print('-' * 79)

# Usage : Removing duplicates from other containers
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
s = set(lst)
print("remove duplicates:", s)

# Empty set : 
s1 = set()
s2 = {}
print("Empty set        :", s1, type(s1), s2, type(s2))

# frozenset() : CRUD operations are unavailable
fset_01 = frozenset({"Jimny", "Thar", "Gurkha"})
print("frozenset        :", fset_01)

for idx, element in enumerate(fset_01):
    print(idx, element)

print('-' * 79)