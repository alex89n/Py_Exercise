import sys
import time
import postekPrinter

PRINTER_PORT = "COM4"
PRINTER_PORT_2 = "COM9"
PRINTER_BAUDRATE = 38400

if __name__ == "__main__":

    SN = "784561B7FEAE"
    SID = "01RHIOHVZPSSEZSX"
    
    template1 = ""
    template2 = "Gift Box"
    template3 = "DOC400el User Manual"
    prnt = postekPrinter.postekPrinter(PRINTER_PORT, PRINTER_BAUDRATE)
    prnt_2 = postekPrinter.postekPrinter(PRINTER_PORT_2, PRINTER_BAUDRATE)

    if prnt.open():
        print "Serijska veza je uspostavljena! " + PRINTER_PORT
        # prnt.setTemplate(template)
        prnt.printDeviceLabel(SN)
        prnt.printGiftBoxLabel(SN)
        prnt.printUserManualLabel(SN, SID)
        # prnt.printFailedLabel(SN, str(4))
        
        # text1 = "REV002 1"
        # text2 = "3934 LMT"
        # copies = 1
        # prnt.printOtherLabel(text1, text2, copies)
        prnt.close()
    else:
        print "Greska! Serijska veza nije uspostavljena! " + PRINTER_PORT

    # if prnt_2.open():
        # print "Serijska veza je uspostavljena! " + PRINTER_PORT_2
        # # prnt.setTemplate(template)
        # prnt_2.printDeviceLabel(SN, template1)
        # prnt_2.printGiftBoxLabel(SN, template2)
        # prnt_2.printUserManualLabel(SN, SID, template3)
        # # prnt.printFailedLabel(SN, str(4))
        
        # # text1 = "REV002 1"
        # # text2 = "3934 LMT"
        # # copies = 1
        # # prnt.printOtherLabel(text1, text2, copies)
        # prnt_2.close()
    # else:
        # print "Greska! Serijska veza nije uspostavljena! " + PRINTER_PORT_2
 