'''
This script is...
'''

import os
import datetime
import glob2

# print(os.listdir())
# print(dir(os))

def create_file(_file):
    with open(str(file_name) + ".txt", 'a') as file:
        file.write(str(_file) + "\n")

file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")

for item in glob2.glob("*.txt"):
    with open(item, 'r') as f:
        create_file(f.read())
