# Python's Garbage Collection :
# Ref : https://stackify.com/python-garbage-collection/

import sys
import gc


print('-' * 79)
# Memory
n1 = 2
n2 = 2200002344245
n3 = 22345.67539
c1 = 'C'
s1 = "dummy string"
lst1 = [1, 32, 456, "test string", 999]
print("Memory       :", sys.getsizeof(n1), sys.getsizeof(n2), sys.getsizeof(n3))
print("Memory       :", sys.getsizeof(c1), sys.getsizeof(s1), sys.getsizeof(lst1))
print("Memory       :", sys.getsizeof(True), sys.getsizeof(None))
print('-' * 79)

# Reference counting
test_string = "Test string."
ref_01 = test_string
ref_02 = ref_01
print("Reference count :", sys.getrefcount(test_string))
print('-' * 79)

# GC
print("GC Threshold :", gc.get_threshold())
print("GC Count     :", gc.get_count())
# Forcing GC
print("GC Collect   :", gc.collect())
print("GC Count     :", gc.get_count())


print('-' * 79)