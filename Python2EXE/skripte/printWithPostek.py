import sys
import time
import postekPrinter

PRINTER_PORT = "COM9"
PRINTER_BAUDRATE = 38400

if __name__ == "__main__":

    SN = "78456153RFC36"
    SID = "01DJNTPQKUSJYKUS"
    template1 = "C:\\Shared\\Printer\\DOC400 label Device"
    template2 = "C:\\Shared\\Printer\\DOC400 label Gift Box"
    template3 = "C:\\Shared\\Printer\\DOC400 label User Manual"
    prnt = postekPrinter.postekPrinter(PRINTER_PORT, PRINTER_BAUDRATE)
    
    barcode = "RT61000001"
    test = "RST_And_Buzz"

    if prnt.open():
        print "Serijska veza je uspostavljena!"
        # prnt.setTemplate(template)
        # prnt.printDeviceLabel(SN, template1)
        # prnt.printGiftBoxLabel(SN, template2)
        # prnt.printUserManualLabel(SN, SID, template3)
        prnt.printFailedLabel(barcode, test)
        prnt.close()
    else:
        print "Greska! Serijska veza nije uspostavljena!"
 