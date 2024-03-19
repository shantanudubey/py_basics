import sys
import getopt


print('-' * 79)
# Python help about any function
help(print)
print('-' * 79)

print('-' * 79)
# Run this file by moving into this folder and typing :
#   command : python .\cmds.py Hello Python 3.11
#   output  : Commandline info >> argv:  ['.\\cmds.py', 'Hello', 'Python', '3.11']

print("version  : ", sys.version)
print("argv     :", sys.argv)
# argv[0] contains the name of the file so skipping it
print("argv[1:] :", sys.argv[1:])


# getopt module is used to parse commandline with flexibility
# Sample :  py .\cmds.py -s Nokia -t Apple -h Delta word1 word2 46546 4646
try:
    options, arguments = getopt.getopt(sys.argv[1:], 'hs:t:')
except getopt.GetoptError as e:
    print("Invalid syntax!", e.msg)
else:
    print("options  :", options)
    print("arguments:", arguments)

print('-' * 79)
sys.exit()

