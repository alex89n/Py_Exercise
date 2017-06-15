import csv
import serial

input_file = "gw_list.csv"
output_file = "cloud_list.csv"

ser = serial.Serial(
    port = 'COM11',\
    baudrate = 9600,\
    parity = serial.PARITY_NONE,\
    stopbits = serial.STOPBITS_ONE,\
    bytesize = serial.EIGHTBITS,\
    timeout=3)
print "\nConnected to: " + ser.portstr
print "Start scaning...\n"

def serialRead(_ser):
    line = ""
    while True:
        for c in _ser.read():
            line += c
            if c == '\r':
                return line[:len(line)-1]
                line = ""
                break

with open(input_file, 'r') as file:
    data = csv.reader(file, delimiter=';')
    
    dict = {}
    # i = 1
    for row in data:
        # print str(i)+ ". " + row[1] + " " + row[2]
        # i += 1 
        dict[row[1]] = row[2]
        
    print ""

while True:
    SN = serialRead(ser)[3:]
    # print SN

    with open(output_file, 'a') as final:
        for key in dict:
            if key == SN:
                final.write("doc400;" + key + ";" + dict[key] + ";obloliving-doc400;1.0.0\n")
                print  key + " " + dict[key] + "\n"
                key_found = True
                break
            else: 
                key_found = False
        
        if not key_found:
            print "Error - " + SN + " NOT FOUND!\n"
            
ser.close()