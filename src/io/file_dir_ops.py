# File and Directory Operations :
import os, time
import shutil


FOLDER_NAME = "test_folder"
FILE_NAME = "test_file.txt"
NESTED_PATH = ".\\test_01\\test_02\\test_03"
FILE_TIME_TESTING = "time_testing.txt"

print('-'*79)
print("OS   :", os.name)
print("OS   :", os.getcwd())
# Current directory :   .
print("OS   :", os.listdir('.'))
# Parent directory  :   ..
print("OS   :", os.listdir('..'))

if os.path.exists(FOLDER_NAME):
    print("OS   :", FOLDER_NAME, "already exists.")
else:
    os.mkdir(FOLDER_NAME)
    print("OS   :", FOLDER_NAME, "directory created.")

print('-'*79)

# Create more directories
os.chdir(FOLDER_NAME)
print("DIR Changed  :", os.getcwd())

if(os.path.exists(NESTED_PATH)):
    print("OS   :", NESTED_PATH, "already exists.")
else:
    os.makedirs(NESTED_PATH)
    print("OS   :", NESTED_PATH, "directories created.")

with open(FILE_NAME, "w") as f:
    f.write("Having one child makes you a parent...")
    f.write("Having two you are a referee.")
    f.close()

stats = os.stat(FILE_NAME)
print("OS   :", stats)
print("size :", stats.st_size)

os.rename(FILE_NAME, "file_001")
shutil.copyfile("file_001", "file_002")
os.remove("file_001")
os.rename("file_002", FILE_NAME)

cur_path = os.path.abspath('.')
cur_path = os.path.join(cur_path, FILE_NAME)
if os.path.isfile(cur_path):
    print("OS   :", FILE_NAME, "exists at :", cur_path)
else:
    print("OS   : File not found at :", cur_path)

print('-'*79)


# Times : This is epoch time in seconds
created_at = os.path.getctime(FILE_TIME_TESTING)
modified_at = os.path.getmtime(FILE_TIME_TESTING)
accessed_at = os.path.getatime(FILE_TIME_TESTING)

# Accessing the file without modifying
with open(FILE_TIME_TESTING, "r") as f:
    print(f.read())
    f.close()

# Convert epoch seconds to local time
print("Created  :", time.ctime(created_at))
print("Modified :", time.ctime(modified_at))
print("Accessed :", time.ctime(accessed_at))

print('-'*79)
