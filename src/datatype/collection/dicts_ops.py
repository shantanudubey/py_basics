"""
Dictionaries : Mutable, ordered(using keys) collection of key:value pairs
    - Known as maps or associative arrays.
    - keys should be unique and immutable like numbers, strings, tuples
        tuples can be used as keys but can't contain a list
    - Can be nested
    - Values can be changed in place but not keys.
    - Cannot be sliced/subscripted since indexing is based on keys not position.
    - Concat, merge doesn't work as subscripting doesn't work.
    - Comparison doesn't work.
    - reversed() works but based on keys as that's how its indexed
    - CRUD available
"""
import operator


print('-' * 79)

dict_str_key = {"key_01":10, "key_02":20, "key_03":30}
dict_num_key = {111:"test_01", 222:"test_02", 11:"test_03"}
dict_tup_key = {(100,200):"loc_03", (50, 100):"loc_02", (0,0):"loc_01"}
print("dict         :", dict_str_key)
print("dict         :", dict_num_key)
print("dict         :", dict_tup_key)
print("access       :", dict_tup_key[0,0], dict_num_key[11], dict_str_key["key_03"])

# Sorting : default sorting is on keys
lst = sorted(dict_num_key)
print("sorted       :", lst)
lst = sorted(dict_num_key.keys())
print("sorted keys  :", lst)
lst = sorted(dict_num_key.values(), key=operator.itemgetter(1))
print("sorted values:", lst)

# Unpacking : using * will only unpack the keys, we need to use ** to unpack values too
dict_temp = {*dict_str_key, *dict_num_key, *dict_tup_key}
print("unpack keys  :", dict_temp)
dict_temp = {**dict_str_key, **dict_num_key, **dict_tup_key}
print("unpack values:", dict_temp)

# Shortcut to create a dict with different keys from a list and same values
lst = ["hi", "hello", "hola", "hej"]
dict_temp.clear()
dict_temp = dict_temp.fromkeys(lst, 8)
print("shortcut     :", dict_temp) 
print('-' * 79)

# CRUD
# Create
dict_temp = {"key_01":"value_01", "key_02":"value_02", "key_03":"value_03"}
dict_temp["temp"] = "XX"
dict_temp["temp1"] = "YY"
dict_temp["temp2"] = "ZZ"
print("Create   :", dict_temp)
# Retrieve
print("Retrieve :", dict_temp["key_01"], dict_temp.get("key_02"))
# Update
dict_temp["temp"] = "GG"
print("Update   :", dict_temp)
# Delete
del(dict_temp["temp"])
dict_temp.pop("temp1")
dict_temp.popitem()
print("Delete   :", dict_temp)
print('-' * 79)

# Traversal : default is keys
for item in dict_temp:
    print(item)

# Using values
for item in dict_temp.values():
    print(item)

# Using both : items()
for item in dict_temp.items():
    print(item, type(item))

for key, value in dict_temp.items():
    print(f"{key:<10}:{value:>10}".format(key, value))

for key, value in dict_tup_key.items():
    print(key, value)
print('-' * 79)

# Specials : 

# Adding multiple values to a key
# By defining values as lists and using lists features
dict_temp["key_03"] = ["value_03"]
dict_temp["key_03"] += ["aval_1"]
# Using extend feature of lists
dict_temp["key_03"].extend(["aval2"])
print("Specials :", dict_temp)


print('-' * 79)
