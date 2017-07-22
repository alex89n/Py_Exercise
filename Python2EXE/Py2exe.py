import os
import sys

if len(sys.argv)>1:
    None
else:
    File=input("Witch script do you want to compile:")
    os.system("C:/Python34/Scripts/cxfreeze "+File)
    print("Finish")
    os.system('pause')
