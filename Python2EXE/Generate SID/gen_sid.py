import time
import sys
import serial
import random

# SEC_ID_STUB="01"

def generateSecId(SEC_ID_STUB = "01"):
    secID = SEC_ID_STUB
    random.seed()
    for i in range(14):
        r = random.random()
        r = r * 25
        if r >= 14:
            r += 1
        secID = secID + chr(65 + int(r))
    return secID

def main():
    loop = 1
    while loop <= 10000:
        print "----------------------------"
        print"Generate SID: \n"
        if len(sys.argv) > 1:
            sid = generateSecId(sys.argv[1])
            print sid
            if sid.find('O') != -1:
                with open("log.txt",'a') as log:
                    log.write(str(loop) +'. ' + sid + "\n")
                # break
            with open("all_sid.txt",'a') as log:
                log.write(str(loop) + "." + sid + "\n")
        else:
            print "Nema ulaznih argumenata"
            break
        loop += 1
if __name__ == "__main__":
  main()