import serial

PRINTER_PARITY = 'N'
PRINTER_TIMEOUT = 10


class postekPrinter:
    def __init__(self, _port, _baudrate):
        self.port = _port
        self.baudrate = _baudrate
        self.parity = PRINTER_PARITY
        self.timeout = PRINTER_TIMEOUT
        self.isopen = False
    
    def open(self):
        self.ser = self.openSerialPort()
        if self.ser.isOpen():
            self.isopen = True
        return self.isopen

    def openSerialPort(self):

        self.ser = serial.Serial()

        self.ser.port      = self.port
        self.ser.baudrate  = self.baudrate
        self.ser.parity    = self.parity
        self.ser.xonxoff   = False
        self.ser.rtscts    = False
        self.ser.timeout   = self.timeout
        self.ser.bytesize  = 8
        self.ser.stopbits  = 1
        self.ser.dsrdtr    = False

        try:
            self.ser.open()
        finally:
            return self.ser
    
    def serialWrite(self, _str):
        self.ser.write(_str)

    def printTemplate(self, _template):
        if not self.isopen:
            return False

        if _template != "":
            try:
                f = open (_template, 'rb')
            except:
                return False
            try:
                temp = f.read(255)
                while temp:
                    self.serialWrite(temp)
                    temp = f.read(255)
            except:
                f.close()
                print "exception"
                return False

            f.close()
            
        return True
            
    def printDeviceLabel(self, _sn, _template = ""):
        # Device label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("JF\r\n")
        # self.serialWrite("GG2,70,\"SSGFX000\"\r\n")
        self.serialWrite("B15,249,0,1,2,4,56,N,\""+_sn+ "\"\r\n")    
        self.serialWrite("A285,247,2,2,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A425,66,2,1,1,1,N,\""+_sn[len(_sn)-6:]+ "\"\r\n")
        self.serialWrite("W1\r\n")
        # self.serialWrite("GK\"SSGFX000\"\r\n")
        
    def printGiftBoxLabel(self, _sn, _template = ""):
        # Gift Box label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("JF\r\n")
        # self.serialWrite("GG24,17,\"SSGFX000\"\r\n")
        self.serialWrite("B15,249,0,1,2,4,56,N,\""+_sn+ "\"\r\n")    
        self.serialWrite("A285,247,2,2,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A425,166,2,2,1,1,N,\""+_sn[len(_sn)-6:]+ "\"\r\n")
        self.serialWrite("W1\r\n")
        # self.serialWrite("GK\"SSGFX000\"\r\n")
        
    def printUserManualLabel(self, _sn, _sid, _template = ""):
        # User Manual label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("JF\r\n")
        # self.serialWrite("GG60,18,\"SSGFX000\"\r\n")
        self.serialWrite("B17,240,0,1,2,4,56,N,\""+_sn+ "\"\r\n")    
        self.serialWrite("A297,238,2,2,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A390,210,2,2,1,1,N,\"SID:"+_sid+ "\"\r\n")
        self.serialWrite("b35,40,QR,0,0,o2,r5,m2,g0,s0,\"SN: "+_sn+ " SID: " +_sid+ "\"\r\n")
        self.serialWrite("W1\r\n")
        # self.serialWrite("GK\"SSGFX000\"\r\n")
        
        
    def printFailedLabel(self, _barcode, _test):
        #Printing label for failed test
        self.serialWrite("N\r\n")
        self.serialWrite("A350,250,2,4,1,1,N,\"FAILED\"\r\n")
        self.serialWrite("A400,185,2,4,1,1,N,\"" + str(_barcode) + "\"\r\n")
        self.serialWrite("A500,110,2,3,1,1,N,\"Test: " + _test + "\"\r\n")
        self.serialWrite("W1\r\n")
    
    
    def printOtherLabel(self, _text1, _text2, _copies):
        for copy in range (1,_copies+1):
            self.serialWrite("N\r\n")
            # self.serialWrite("B425,284,2,1,3,5,56,N,\""+_text+ "\"\r\n")    
            self.serialWrite("A500,220,2,1,2,1,N,\""+_text1+ "\"\r\n")
            self.serialWrite("A500,160,2,1,2,1,N,\""+_text2+ "\"\r\n")
            self.serialWrite("W1\r\n")
            

    def close(self):
        if self.isopen:
            self.ser.close()
            self.isopen = False