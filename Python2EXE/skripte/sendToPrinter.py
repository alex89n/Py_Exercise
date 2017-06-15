import serial

PRINTER_PORT = 'COM9'
PRINTER_BAUDRATE = 9600
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
    except:
        print "Greska u otvaranju porta " + port

    return ser

def serialWrite(_ser, _str):
  for i in range(len(_str)):
    #sys.stdout.write(_str[i])
    _ser.write(_str[i])
    time.sleep(0.01)

template = "c:\\Shared\\Printer\\Barcode_template"

prnSer = openSerialPort(PRINTER_PORT, PRINTER_BAUDRATE, PRINTER_PARITY, 10)
if not prnSer.isOpen():
    print "Greska! Serijska veza sa stampacem nije uspostavljena!"
    sys.exit(1)

f = open (template, 'rb')
x = open ("log", 'wb')
try:
    temp = f.read(255)
    while temp:
        serialWrite(prnSer, temp)
        x.write(temp)
        temp = f.read(255)
finally:
    x.close()
    f.close()
    prnSer.close()
    





    
