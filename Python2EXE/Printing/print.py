import sys
import time
import serial

PRINTER_PORT = 'COM4'
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
    
    # # Pocetna vrednost za x
    # x = 4 
    # # range za y i z
    # y = 5
    # z = 7
    # for y in range(1,y+1):
        # for z in range(1,z+1):
            # serialWrite(ser, "N\r\n")
            # serialWrite(ser, "JB\r\n")    
            # serialWrite(ser, "A480,40,1,5,1,1,N,\"" + str(x) +"." + str(y) + "." + str(z) + "\"\r\n")
            # serialWrite(ser, "A280,40,1,5,1,1,N,\"" + str(x) +"." + str(y) + "." + str(z) + "\"\r\n")
            # serialWrite(ser, "A80,40,1,5,1,1,N,\"" + str(x) +"." + str(y) + "." + str(z) + "\"\r\n")
            # serialWrite(ser, "W1\r\n")
    
    # # pocetna vredost za a
    # a = 1
    # # range za b
    # b = 100
    # for b in range(1,b+1):
        # serialWrite(ser, "N\r\n")
        # serialWrite(ser, "JB\r\n")    
        # serialWrite(ser, "A480,40,1,5,1,1,N,\"" + str(a) +"." + str(b) + "\"\r\n")
        # serialWrite(ser, "A280,40,1,5,1,1,N,\"" + str(a) +"." + str(b) + "\"\r\n")
        # serialWrite(ser, "A80,40,1,5,1,1,N,\"" + str(a) +"." + str(b) + "\"\r\n")
        # serialWrite(ser, "UN\r\n")
        # serialWrite(ser, "W1\r\n")

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
    
	# ugradjeni font
    # serialWrite(ser, "I8,001\r\n")
    # serialWrite(ser, "N\r\n")
    # serialWrite(ser, "H10\r\n")
    # serialWrite(ser, "CF1,M,Monaco\r\n")
    # serialWrite(ser, "A400,100,2,2,2,2,N,\"SXY8/AO\"\r\n")
    # serialWrite(ser, "A400,100,2,2,2,2,N,\"SXY80AO\"\r\n")
    # serialWrite(ser, "g10\r\n")
    # serialWrite(ser, "W1\r\n")
	
    serialWrite(ser, "GG14,6,\"SSGFX000\"\r\n")
    # serialWrite(ser, "B550,274,2,1,4,4,120,N,\"aleksandar.zivkovic@rt-rk\"\r\n")    
    serialWrite(ser, "A540,160,2,1,1,3,N,\"user: aleksandar.zivkovic@rt-rk.com\"\r\n")
    serialWrite(ser, "A540,110,2,1,1,3,N,\"pass: Uak19!Um\"\r\n")
    serialWrite(ser, "W1\r\n")
    serialWrite(ser, "GK\"SSGFX000\"\r\n")
    
    # for i in xrange(2):    
    # Stop za lepljenje na laptop
    # serialWrite(ser, "N\r\n")
    # # serialWrite(ser, "B450,170,2,1,4,4,35,N,\"Start\"\r\n")    
    # serialWrite(ser, "A350,540,2,1,2,3,N,\"aleksandar.zivkovic@rt-rk.com\"\r\n")
    # serialWrite(ser, "A250,10,2,1,2,3,N,\"Uak19!Um\"\r\n")
    # serialWrite(ser, "W1\r\n")
        
        # # Continue    
        # serialWrite(ser, "N\r\n")
        # serialWrite(ser, "B520,274,2,1,4,4,120,N,\"Continue\"\r\n")    
        # serialWrite(ser, "A495,140,2,4,2,3,N,\"Continue\"\r\n")
        # serialWrite(ser, "W1\r\n")
        
        # # Pass
        # serialWrite(ser, "N\r\n")
        # serialWrite(ser, "B450,274,2,1,4,4,120,N,\"Pass\"\r\n")    
        # serialWrite(ser, "A390,140,2,4,2,3,N,\"Pass\"\r\n")
        # serialWrite(ser, "W1\r\n")
        
        # # Fail
        # serialWrite(ser, "N\r\n")
        # serialWrite(ser, "B450,274,2,1,4,4,120,N,\"Fail\"\r\n")    
        # serialWrite(ser, "A390,140,2,4,2,3,N,\"Fail\"\r\n")
        # serialWrite(ser, "W1\r\n")
    
    # serialWrite(ser, "N\r\n")   
    # serialWrite(ser, "A510,285,2,A,2,2,N,\"AMonakOo0\"\r\n")
    # # serialWrite(ser, "A510,225,2,3,2,2,N,\"NIKOLIC\"\r\n")
    # # serialWrite(ser, "A510,145,2,3,2,2,N,\"SERBIA\"\r\n")
    # # serialWrite(ser, "A510,85,2,2,2,2,N,\"+381652939960\"\r\n")
    # serialWrite(ser, "W1\r\n")
    
   
     
    ser.close()
  