# File : Serializing/Deserializing data using JSON

import json
import os


print('-'*79)
FOLDER_NAME = "test_folder"
# change working dir to test_folder
print("File :", os.chdir(FOLDER_NAME))
print("File :", os.getcwd())
FILE_NAME = "test_serializations"

# tuples are serialized as lists but can be converted to a tuple
lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
tpl = ("Ajay", 35, 42500)
dct = {'name':"Dilip", 'age':34, 'salary':43870}

print('-'*79)
# Serializing as JSON : can't serialize multiple objects without convering to custom type
with open(FILE_NAME, "w+") as f:
    json.dump(dct, f)       
    f.seek(0)
    data = json.load(f)
    print("dump/load    :", type(data), data)    
    f.close()

# Serializing as string : can serialize multiple objects
with open(FILE_NAME, "w+") as f:
    s1 = json.dumps(lst)
    s2 = json.dumps(tpl)
    s3 = json.dumps(dct)

    l = json.loads(s1)
    t = json.loads(s2)
    d = json.loads(s3)

    print("dumps/loads  :", l, t, d)    
    f.close()

print('-'*79)