# Python's Garbage Collection :
# Ref : https://stackify.com/python-garbage-collection/

import sys
import gc


# Reference counting
test_string = "Test string."
ref_01 = test_string
ref_02 = ref_01
print("Reference count :", sys.getrefcount(test_string))

#print('-' * 79)
# GC
print("GC Threshold :", gc.get_threshold())
print("GC Count     :", gc.get_count())
# Forcing GC
print("GC Collect   :", gc.collect())
print("GC Count     :", gc.get_count())

