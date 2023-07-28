# File I/O
import os

FILE_NAME = "test_file_io.txt"
FOLDER_NAME = "test_folder"

print('-'*79)
# change working dir to test_folder
print("File :", os.chdir(FOLDER_NAME))
print("File :", os.getcwd())
print("File :", os.getcwdb())
print('-'*79)

# Write to file
msg_01 = "Pay taxes with a smile...\n"
msg_02 = "I tried but they wanted money...\n"
test_data = "line 1\nline 2\nline 3\nline 4\nline 5\nline 6\n"
f = open(FILE_NAME, "w")
f.write(test_data)
f.write(msg_01)
f.write(msg_02)
f.close()
# Read from file
f = open(FILE_NAME, "r")
fd = f.read()
print(fd)
f.close()
print('-'*79)

# Writing/Reading multiple lines and types : 
# We can write in only 2 types of data : Text/Bytes
print("Writing to file :", FILE_NAME)
f = open(FILE_NAME, "w")

msg_03 = "Bad offcials are elected by good citizens who do not vote.\n"
msgs_01 = ["Humpty\n", "Dumpty\n", "Sat\n", "On\n", "a\n", "Wall\n"]
f.write(msg_03)
f.writelines(msgs_01)

# Write multiple types after converting them to string
lst = [11, 22, 33, 44, 55, 66]
tpl = ("Yash", 24, 22000)
d = {'name':"Dilip", 'age':34, 'salary':41000}
f.write(str(lst)+'\n')
f.write(str(tpl)+'\n')
f.write(str(d)+'\n')
f.write(str(99999999)+'\n')
f.close()
print('-'*79)

# Reads all file contents and returns a string
print("Reading contents of file :", FILE_NAME)
f = open(FILE_NAME, "r")
data = f.read()
print(data)
f.close()
print('-'*79)

# Reads n characters, returns a string
f = open(FILE_NAME, "r")
data = f.read(10)
print("Reading 10 chars :", data)
f.close()

# Reads a line, returns a string
f = open(FILE_NAME, "r")
data = f.readline()
print("Reading a line   :", data)
f.close()

# Reads all lines, returns a list
f = open(FILE_NAME, "r")
data = f.readlines()
print("Reading all lines:", type(data))
for line in data:
    print(line, end='') # Since \n is already present in the file
print()
f.close()
print('-'*79)

# Modifying file to trim trailing whitespaces
f = open(FILE_NAME, "r")
data = f.read()

# If there is a trailing whitespace, trim it
if(data[len(data)-1].isspace()):
    m_data = data.rstrip()
    f.close()
    # Write trimmed data to file
    f = open(FILE_NAME, "w")
    f.write(m_data)
    f.close
    # Read the data to confirm
    print("Reading contents of file :", FILE_NAME)
    f = open(FILE_NAME, "r")
    data = f.read()
    print(data)
    f.close()
else:
    f.close()

print('-'*79)

# Using 'with' : Ensures that a file is closed as soon as te usage is over
#   Even if an Exception occurs.
with open(FILE_NAME, "r") as f:
    data = f.readline()
    print(data)

# seek() : moves the seeker position from where the operation will start
#   f.seek(offset, reference) : 
#   offsset     : bytes to skip from ref 
#   reference   : 0(start), 1(current), 2(end) position >> 1,2 binary only
with open(FILE_NAME, "r") as f:
    # Default 
    data = f.read(12)
    print("Seek :", data)
    # 0 : start of file, move 5 characters to the right
    f.seek(4, 0)
    data = f.read(8)
    print("Seek :", data)

# Move 5 characters to the right from the current position
# Since ref : 1, 2 are supported in binary mode only we use that
with open(FILE_NAME, "rb") as f:
    data = f.read(12)
    print("Seek :", data)
    # 1 : current position of the seeker in the file
    f.seek(5, 1)
    data = f.read(10)
    print("Seek :", data)
    # 2 : works from end of file so the contants have to be backtracked
    f.seek(-168, 2)
    data = f.read(13)
    print("Seek :", data)


print('-'*79)