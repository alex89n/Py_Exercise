r'''
This script is nesto.
'''

import os
# print(os.listdir())
# print(dir(os))
import datetime

file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

# file_name.strftime("%Y-%m-%d-%H-%M-%S-%f")

def create_file():
    with open(str(file_name), 'w') as file:
        file.write("")
        
create_file()