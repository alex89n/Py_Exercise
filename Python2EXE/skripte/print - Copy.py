import sys
import time
import serial

PRINTER_PORT = 'COM3'
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

def printMAC(_str):

  _str = _str.replace("-", "")
  serialWrite(ser, "N\n")
  serialWrite(ser, "Q152,16\n")
  #serialWrite(ser, "R\n")
  serialWrite(ser, "D12\n")
  #serialWrite(ser, "S1\n")
  serialWrite(ser, "A305,5,0,2,1,1,N,\"" + _str + "\"\n")
  serialWrite(ser, "B290,25,0,1A,1,3,30,N,\"" + _str + "\"\n")
  serialWrite(ser, "P\n")
  #serialWrite(ser, "^@\n")

  
def serialWrite(_ser, _str):
  _ser.write(_str)
  

def testPrint(_ser):
  serialWrite(_ser, "N\r\n")
  serialWrite(_ser, "B500,220,2,1,3,18,81,N,\"SN: 00037F1133CE\"\r\n")
  serialWrite(_ser, "A460,120,2,4,1,1,N,\"SN:00037F1133CE\"\r\n")
  serialWrite(_ser, "W1\r\n")

if __name__ == "__main__":
  ser = openSerialPort(PRINTER_PORT, PRINTER_BAUDRATE, PRINTER_PARITY, 10)
  if not ser.isOpen():
    print "Greska! Serijska veza nije uspostavljena!"
    sys.exit(1)
  
  
  #print something
  #printMAC("12-34-56-78-9A-BC")
  #testPrint(ser)
  
  template="C:\\Users\\aleksandarn\\Desktop\\Barcode template"
  
  f = open (template, 'rb')
  x = open ("log", 'wb')
  try:
    temp = f.read(255)
    while temp:
      serialWrite(ser, temp)
      x.write(temp)
      temp = f.read(255)
  finally:
    x.close()
    f.close()  

  ser.close()
  
  