import sys
import time
import serial

PRINTER_PORT = 'COM9'
PRINTER_BAUDRATE = 38400
PRINTER_PARITY = 'N'

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
    except serial.SerialException, e:
      print "Greska u otvaranju porta " + port
    except:
      print "Greska: Nepoznata!"
      
    return ser

    
def serialWrite(_ser, _str):
    _ser.write(_str)


if __name__ == "__main__":
    ser = openSerialPort(PRINTER_PORT, PRINTER_BAUDRATE, PRINTER_PARITY, 10)
    if not ser.isOpen():
        print "Greska! Serijska veza nije uspostavljena!"
        sys.exit(1)
  
    # template="C:\\Shared\\Printer\\DOC400 label SSID"
    
    # SN = "REV001-1"
        
    # f = open (template, 'rb')
    # x = open ("log", 'wb')
    # try:
      # temp = f.read(255)
      # while temp:
        # serialWrite(ser, temp)
        # x.write(temp)
        # temp = f.read(255)
    # finally:
      # x.close()
      # f.close()  

    # ser.close()
    
    # serialWrite(ser, "N\r\n")
    # serialWrite(ser, "GG14,6,\"SSGFX000\"\r\n")
    # serialWrite(ser, "B405,284,2,1,2,4,56,N,\"SN:"+SN+ "\"\r\n")    
    # serialWrite(ser, "A221,220,2,1,1,1,N,\"SN:"+SN+ "\"\r\n")
    # serialWrite(ser, "A425,186,2,1,1,1,N,\""+SN[8:]+ "\"\r\n")
    # serialWrite(ser, "W1\r\n")
    # serialWrite(ser, "GK\"SSGFX000\"\r\n")
    
    
    # for x in range(1,21):
        # serialWrite(ser, "N\r\n")   
        # serialWrite(ser, "A500,195,2,5,1,1,N,\"REV002-"+str(x)+ "\"\r\n")
        # serialWrite(ser, "W1\r\n")
    
    serialWrite(ser, "N\r\n")   
    serialWrite(ser, "b250,100,QR,0,0,o2,r5,m2,g0,s0,\"SN: 784561536EAD Security ID: 01DJNTPQKUSJYKUS\"\r\n")
    serialWrite(ser, "W1\r\n")
     
    ser.close()
  