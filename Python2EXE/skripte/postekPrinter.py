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
            
    def printDeviceLabel(self, _sn, _template):
        # Device label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("GG14,6,\"SSGFX000\"\r\n")
        self.serialWrite("B405,284,2,1,2,4,56,N,\"SN:"+_sn+ "\"\r\n")    
        self.serialWrite("A241,220,2,1,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A425,186,2,1,1,1,N,\""+_sn[len(_sn)-4:]+ "\"\r\n")
        self.serialWrite("W1\r\n")
        self.serialWrite("GK\"SSGFX000\"\r\n")
        
    def printGiftBoxLabel(self, _sn, _template):
        # Gift Box label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("GG12,21,\"SSGFX000\"\r\n")
        self.serialWrite("B405,304,2,1,2,4,56,N,\"SN:"+_sn+ "\"\r\n")    
        self.serialWrite("A241,240,2,1,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A425,63,2,1,1,1,N,\""+_sn[len(_sn)-4:]+ "\"\r\n")
        self.serialWrite("W1\r\n")
        self.serialWrite("GK\"SSGFX000\"\r\n")
        
    def printUserManualLabel(self, _sn, _sid, _template):
        # User Manual label
        self.printTemplate(_template)
        self.serialWrite("N\r\n")
        self.serialWrite("GG40,14,\"SSGFX000\"\r\n")
        self.serialWrite("B405,300,2,1,2,4,56,N,\"SN:"+_sn+ "\"\r\n")    
        self.serialWrite("A241,238,2,1,1,1,N,\"SN:"+_sn+ "\"\r\n")
        self.serialWrite("A392,213,2,1,1,1,N,\"SecurityID:"+_sid+ "\"\r\n")
        self.serialWrite("b23,40,QR,0,0,o2,r5,m2,g0,s0,\"SN: "+_sn+ " Security ID: " +_sid+ "\"\r\n")
        self.serialWrite("W1\r\n")
        self.serialWrite("GK\"SSGFX000\"\r\n")
        
        
    def printFailedLabel(self, _barcode, _test):
        #Printing label for failed test
        self.serialWrite("N\r\n")
        self.serialWrite("A500,250,2,3,1,1,N,\"Test: " + _test + "\"\r\n")
        self.serialWrite("A350,185,2,4,1,1,N,\"FAILED\"\r\n")
        self.serialWrite("A400,120,2,4,1,1,N,\"" + str(_barcode) + "\"\r\n")
        self.serialWrite("W1\r\n")
        

    def close(self):
        if self.isopen:
            self.ser.close()
            self.isopen = False