import sys
import time
import serial

PORT = 'COM11'
BAUDRATE = 38400

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

def serialRead(_ser):
    line = ""
    while True:
        for c in _ser.read():
            line += c
            if c == '\r':
                return str(line)
                line = ""
                break


if __name__ == "__main__":
    ser = openSerialPort(PORT, BAUDRATE)    
    # if not ser.isOpen():
        # print "Greska - Serijska veza nije uspostavljena!"
        # sys.exit(1)
    
    # print("connected to: " + ser.portstr)
    proba = serialRead(ser)
    print proba

     
    ser.close()
  