import sys
import time
import postekPrinter
import csv

PRINTER_PORT = "COM4"
PRINTER_BAUDRATE = 38400

if __name__ == "__main__":

    SN = "784561B7E530"
    SID = "01RHIOHVZPOSEZSX"
    
    # Label templates
    template1 = "Cockpit label Device"
    template2 = "Cockpit label Gift Box"
    template3 = "Cockpit label User Manual"
    
    # .csv file with SN and SID
    file = "16Gw_csv_NETIC.csv"
    col = []
    with open(file, 'r') as data:
        f = csv.reader(data, delimiter = ';')
        for row in f:
            # print row
            col.append(row)    
    
    prnt = postekPrinter.postekPrinter(PRINTER_PORT, PRINTER_BAUDRATE)

    if prnt.open():
        print "Serijska veza je uspostavljena!"        
        for i in range(0,len(col)):
            print col[i][1]
            print col[i][2]
            print
            # prnt.printDeviceLabel(col[i][1], template1)
            prnt.printGiftBoxLabel(col[i][1], template2)
            prnt.printUserManualLabel(col[i][1], col[i][2], template3)
        
        # text1 = "REV002 1"
        # text2 = "3934 LMT"
        # copies = 1
        # prnt.printOtherLabel(text1, text2, copies)
        prnt.close()
    else:
        print "Greska! Serijska veza nije uspostavljena!"
 