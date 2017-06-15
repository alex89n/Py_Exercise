import sys
import time
import Queue
import serial
import random	
import threading

#---------------------- Serial port settings-----------------------------
BOARD_PORT = 'COM1'
BOARD_BAUDRATE = 115200
BOARD_PARITY = 'N'

#---------------------- LAN settings-------------------------------------

SERVER_IP = "192.168.1.103"
BOARD_IP = "192.168.1.130"

#---------------------- TFTP settings------------------------------------

TFTP_DIR="c:\\TFTP-Root\\"
TFTP_SEC_FILE=TFTP_DIR + "security.txt"


#------------------------- Timings --------------------------------------
UBOOT_WAIT      = 60            #wait time in seconds
WAIT_TIME       = 80     
BOOT_WAIT       = 200           #wait time in seconds

COMMAND_PAUSE   = 1
#------------------------- Commands --------------------------------------
ENTER_CHAR = "\r"
tftpComm = "tftp 0x80060000 uboot-env.bin&&erase 0x9f040000 +$filesize&&cp.b $fileaddr 0x9f040000 $filesize" + ENTER_CHAR
resetComm = "reset" + ENTER_CHAR
bootComm = "boot" + ENTER_CHAR
runFlashComm = "run lu && run lk && run lf && run ldata && run lgf && run lgk" + ENTER_CHAR
setServerIp = "set serverip " + SERVER_IP + ENTER_CHAR
setBoardIp = "set ipaddr " + BOARD_IP + ENTER_CHAR
runLsec = "run lsec" + ENTER_CHAR

#---------------------- Other settings-----------------------------------

SEC_ID_STUB="01"
#VERBOSE=True
VERBOSE=False

#------------------  Serial port funciton(s) ------------------------------
def openSerialPort(port, baudrate, parity = 'N', timeout = 10):

    ser = serial.Serial()
    ser.port      = port
    ser.baudrate  = baudrate
    ser.parity    = parity
    ser.xonxoff   = False
    ser.rtscts    = False
    ser.timeout   = timeout
    ser.bytesize  = 8
    ser.stopbits  = 1
    ser.dsrdtr    = False

    try:
        ser.open()
    finally:
        return ser
  
class BoardSer:  
  
    def __init__(self, port, baudrate, parity, timeout):
        self.port = port
        self.baudrate= baudrate
        self.timeout = timeout
        self.parity = parity
        self.threadActive = True

    def connect(self):
        self.ser = openSerialPort(self.port, self.baudrate, self.parity, self.timeout)
        if self.ser.isOpen():
            self.threadComm = threading.Thread(target=self.commThread)
            self.threadComm.setDaemon(True)
            self.threadComm.setName('serial->socket')
            self.threadComm.start()
            self.queue = Queue.Queue()
            self.ser.flushInput()
            self.ser.flushOutput()
        return  self.ser.isOpen()
    
    def close(self):
        self.threadActive = False
        self.ser.close()

    def commThread(self):

        #print "Thread started!"
        self.ser.flushInput()

        while (self.threadActive):
            byte = self.ser.read(1)
            self.queue.put(byte)
            #print "Thread stopped!" 
        
    def read(self, maxcount):
        retVal = ""
      
        if not self.queue.empty():
            for i in range(maxcount):
                retVal = retVal + self.queue.get()
      
        if VERBOSE:
            if retVal != "":
                sys.stdout.write(retVal)
      
        return retVal
      
    def write(self, _str):
        self.ser.write(_str)
        self.ser.flushOutput()

#------------------------- user message function ----------------------------
def printMessage(_str):
    #for now, just send message to stdout
    if not VERBOSE:
        print _str

def printErrorMessage(_str):
    #for now, just send message to stdout
    print _str

#------------------------- Functions working with board ---------------------

def EnterUboot(_port):

    tStart = time.time()
    ubootInProgress = True
    message = ""
    hitDone = False

    while ubootInProgress:

        message = message + _port.read(1)
        pos = message.find("Hit any key to stop autoboot")

        if (0 <= pos):
            if not hitDone:
                time.sleep(0.1)
                _port.write(ENTER_CHAR)
                hitDone = True
            time.sleep(0.2)
            count = message.count("ath>", pos)
            if (count > 0):
                ubootInProgress = False

        tCur = time.time()
        elapsedTime = tCur - tStart
        if elapsedTime > UBOOT_WAIT:
            return False
        
    #printMessage(message) #Branislav: FOR DEBUG

    return True
    
def setIpAddrs(_ser):
    _ser.write(setServerIp)
    time.sleep(COMMAND_PAUSE)
    _ser.write(setBoardIp)
    time.sleep(COMMAND_PAUSE)
    
def generateSecId():
    secID = SEC_ID_STUB
    random.seed()
    for i in range(14):
        r = random.random()
        r = r * 26
        secID = secID + chr(65 + int(r))
    return secID
  
def flashWait(_ser, _fileName, _confirmation, _count, _timeout):
    boardFlashed = False
    message = ""
    tStart = time.time()
    while not boardFlashed:
        message = message + _ser.read(1)
        if len(message) > 0:
            pos = message.find(_fileName)
            if 0 <= pos:
                count = message.count(_confirmation, pos)
                if count >= _count:
                    boardFlashed = True
                    #printMessage(message)  #Branislav: FOR DEBUG
        tCur = time.time()
        tElapsed = tCur - tStart
        if tElapsed > _timeout:
            #printMessage(message)  #Branislav: FOR DEBUG
            return False
    return True
    
def main():

    printMessage("Opening serial port...")

    boardSer = BoardSer(BOARD_PORT, BOARD_BAUDRATE, BOARD_PARITY, 10)
    portOpened = boardSer.connect()
    if not portOpened:
        printErrorMessage("Error! Could not open serial port " + BOARD_PORT)
        sys.exit(1)

    printMessage("Waiting for uboot...")

    status = EnterUboot(boardSer)
    if  not status:
        printErrorMessage("Error! Uboot not reached!")
        boardSer.close()
        sys.exit(1)

    printMessage("Set IP addresses")

    setIpAddrs(boardSer)

    printMessage("Flashing Env Variables")

    boardSer.write(tftpComm)

    status = flashWait(boardSer, "uboot-env.bin", "done", 2, WAIT_TIME)
    if not status:
        printErrorMessage("Error: Could not flash env variables!")
        #printMessage(message)  #Branislav: FOR DEBUG
        boardSer.close()
        sys.exit(1)
        

    printMessage("Reset...")
    boardSer.write(resetComm)

    printMessage("Waiting for uboot...")

    status = EnterUboot(boardSer)
    if  not status:
        printErrorMessage("Error! Uboot not reached!")
        boardSer.close()
        sys.exit(1)
        
    printMessage("Set IP addresses")
    setIpAddrs(boardSer)
    
    #prepare security id
    secId = generateSecId()
    #print ("Security ID is: " + secId)

    try:
        f = open(TFTP_SEC_FILE, 'w')
    except:
        printMesssage("Error! Could not open security file!")
        boardSer.close()
        sys.exit(1)
    f.write(secId)
    f.close()
    
    printMessage("Flashing Security...")
    boardSer.write(runLsec)
    
    status = flashWait(boardSer, "security.txt", "OK", 2, WAIT_TIME)
    if not status:
        printErrorMessage("Error: Could not flash security!")
        boardSer.close()
        sys.exit(1)
   
    time.sleep(5)
    printMessage("Flashing Images...")
    boardSer.write(runFlashComm);
    
    printMessage("\tu-boot.bin")
    status = flashWait(boardSer, "u-boot.bin", "done", 1, WAIT_TIME)
    if status:
        printMessage("\tvmlinux.lzma.uImage")
        status = flashWait(boardSer, "vmlinux.lzma.uImage", "OK", 2, WAIT_TIME)
    if status:
        printMessage("\tcus531-nand-jffs2")
        status = flashWait(boardSer, "cus531-nand-jffs2", "OK", 2, WAIT_TIME)
    if status:
        printMessage("\tdata.ubi")
        status = flashWait(boardSer, "data.ubi", "OK", 2, WAIT_TIME)
    if status:
        printMessage("\tg-cus531-nand-jffs2")
        status = flashWait(boardSer, "g-cus531-nand-jffs2", "OK", 2, WAIT_TIME)
    if status:
        printMessage("\tg-vmlinux.lzma.uImage")
        status = flashWait(boardSer, "g-vmlinux.lzma.uImage", "OK", 2, WAIT_TIME)
    
    if not status:
        printErrorMessage("Error: Image download failed!")
        boardSer.close()
        sys.exit(1)
  
    printMessage("Booting")

    time.sleep(2)
    boardSer.write(bootComm)
    status = flashWait(boardSer, "procd: - init -", "procd: - init complete -", 1, BOOT_WAIT);
    if not status:
        printErrorMessage("Error: Failed to boot")
    else:
        printMessage("Done!")

    boardSer.close()
    time.sleep(1)

if __name__ == "__main__":
    main()
