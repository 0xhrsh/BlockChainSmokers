import asciitable
import os
from string import ascii_uppercase
import sys

PATH_TEMPLATE = '{}:/key.txt'
for drive in ascii_uppercase[:-24:-1]: # letters 'Z' down to 'D'
    file_path = PATH_TEMPLATE.format(drive)
    if os.path.exists(file_path):
        f=open(file_path,"r")
        key=f.read()
        break
else:
    print('error, file not found')
    sys.exit(1)
flag=True
for i in range(3):
	if int(key[i+1])!=2*int(key[i]):
		flag=False
		break
if flag:
	print("key validated")
else:
	print("you are a fraud")