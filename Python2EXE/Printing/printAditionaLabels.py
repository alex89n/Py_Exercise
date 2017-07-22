import sys
import time
import postekPrinter

# python -m dbReadExample.py compile

PRINTER_PORT = "COM4"
PRINTER_BAUDRATE = 38400

template1 = "\\\192.168.1.3\\Shared\\Printer\\DOC400 label Device"
# template1 = "d:\\Shared\\Printer\\DOC400 label Device"

if __name__ == "__main__":
    while 1:
        SN = str(raw_input("\nPlease input FAIL BARCODE LABEL number: "))
        if len(SN) == 12:
            print "\n" + SN
            prnt = postekPrinter.postekPrinter(PRINTER_PORT, PRINTER_BAUDRATE)
            if prnt.open():
                print "\nSerial connection OK - Wait for Label"
                prnt.printDeviceLabel(SN, template1)        
            else:
                print "\nError - Wrong Connection, check " + PRINTER_PORT
                time.sleep(0.5)
        else:
                print "Error - Incorect BARCODE number, try again!"
                time.sleep(0.5)