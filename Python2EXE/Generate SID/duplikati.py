import time
import sys
import serial
import random

dict = {}
with open("all_sid.txt",'r') as f:
    file = f.readlines()
    print file
    for i in range(0,len(file)):
        file2 = file[i].split(".")
        file2[1] = file2[1][:-2]
        dict[file2[1]] = file2[0]
        print file2
    

    print dict
    for key in dict:
        with open("dict_log.txt",'a') as f:
            f.write(key + " ------ " + dict[key] + "\n")