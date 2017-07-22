import time
import array
import os
import os.path
import shutil

TEMP1V_CONST = 650
TEMP1V_TOLERANCE = 100
TEMP_HIGH = 4500
TEMP_LOW = -500

def repackHex(num):
    tmp = ""
    for i in range(0, len(num)/2):
        j = (len(num) - 2) - (i*2)
        tmp += num[j:(j+2)]   
    print "tmp hex =  " + str(tmp)
    if len(num) > 3:
        return tmp
    else:    
        num = int(tmp, 16)
        print "tmp int =  " + str(num)
        return num




FILE_PATH="C:\\Users\\aleksandarn\\Desktop\\Python2EXE\\"
with open(FILE_PATH + 'RF_test_example.txt', 'r+') as file:
    lines = file.readlines()
print "lines:"
print lines
print "------------------------------------------------------------\n"

# lines = ''
    # for i in range(1, 4):
        # lines = device.handler("SerialGeneric", "GET", "response", "0")
        # if lines.find('RSSI:') >= 0:
            # break
        # time.sleep(3)

#Taster test
line = lines[0]
# print line
dataIndex = line.find('DATA:01')
tasterState = line[(dataIndex+ len("DATA:01")):(dataIndex+ len("DATA:01") + 2)]
print "rfmsgID = 1"
print "tasterState = " + tasterState
if tasterState != "00":
    print "ERROR"
print "------------------------------------------------------------\n"

#RF test
line = lines[1]
# print line
dataIndex = line.find('DATA:02')
print "rfmsgID = 2"
dutSN = line[(dataIndex + len("DATA:02")):(dataIndex + len("DATA:02") + 16)]
print "dutSN =  " + str(dutSN)

dutSN = repackHex(dutSN)
print "dutSN =  " + str(dutSN)

devID = line[(dataIndex + len("DATA:02") + len(dutSN)):(dataIndex + len("DATA:02") + len(dutSN) + 2)]
print "devID =  " + str(devID)

hwVersion = line[(dataIndex + len("DATA:02") + len(dutSN) + len(devID)):(dataIndex + len("DATA:02") + len(dutSN) + len(devID) + 2)]
print  "hwVersion =  " + str(hwVersion)

stackVersion = line[(dataIndex + len("DATA:02") + len(dutSN) + len(devID) + len(hwVersion)):(dataIndex + len("DATA:02") + len(dutSN) + len(devID) + len(hwVersion) + 2)]
print  "stackVersion =  " + str(stackVersion)

appVersion = line[(dataIndex + len("DATA:02") + len(dutSN) + len(devID) + len(hwVersion) + len(stackVersion)):(dataIndex + len("DATA:02") + len(dutSN) + len(devID) + len(hwVersion) + len(stackVersion) + 2)]
print  "appVersion =  " + str(appVersion)
    
print "------------------------------------------------------------\n"

#Calibration
line = lines[2]
# print line
dataIndex = line.find('DATA:')
rfmsgID = line[(dataIndex+len("DATA:")):(dataIndex+ len("DATA:") + 2)]
print rfmsgID
if rfmsgID == "03":
    adcOffset = line[(dataIndex + len("DATA:") + len(rfmsgID)):(dataIndex + len("DATA:") + len(rfmsgID) + 2)]
    print "adcOffset =  " + str(adcOffset)
    adcConst = line[(dataIndex + len("DATA:") + len(rfmsgID) + len(adcOffset)):(dataIndex + len("DATA:") + len(rfmsgID) + len(adcOffset) + 4)]
    print "adcConst hex =  " + str(adcConst)
    
    adcConst = repackHex(adcConst)
    
    print "adcConst =  " + str(adcConst)
else:
    print "ERROR"
print "------------------------------------------------------------\n"

#1V Temp test
line = lines[3]
# print line
dataIndex = line.find('DATA:')
rfmsgID = line[(dataIndex+len("DATA:")):(dataIndex+ len("DATA:") + 2)]
print rfmsgID
if rfmsgID == "04":
    temp1V = line[(dataIndex + len("DATA:") + len(rfmsgID)):(dataIndex + len("DATA:") + len(rfmsgID) + 4)]
    print "temp1V hex =  " + str(temp1V)
    
    temp1V = repackHex(temp1V)
    print "temp1V =  " + str(temp1V)
    
    if not ((TEMP1V_CONST - TEMP1V_TOLERANCE) < temp1V < (TEMP1V_CONST + TEMP1V_TOLERANCE)):
        print "ERROR"

else:
    print "ERROR"
print "------------------------------------------------------------\n"


#Temp test
line = lines[4]
# print line
dataIndex = line.find('DATA:')
rfmsgID = line[(dataIndex+len("DATA:")):(dataIndex+ len("DATA:") + 2)]
print rfmsgID
if rfmsgID == "05":
    temp = line[(dataIndex + len("DATA:") + len(rfmsgID)):(dataIndex + len("DATA:") + len(rfmsgID) + 4)]
    print "temp hex =  " + str(temp)
    
    temp = repackHex(temp)
    print "temp =  " + str(temp)
    
    if not (TEMP_LOW < temp < TEMP_HIGH):
        print "ERROR"

else:
    print "ERROR"
print "------------------------------------------------------------\n"

dataIndex = line.find('RSSI:')
print dataIndex
print line[dataIndex]
print ""
rssi_s = ''
if dataIndex != -1:
    for i in range(0, 4):
        if line[dataIndex + len('RSSI:')+i] != ' ':
            rssi_s += str(line[dataIndex+len('RSSI:')+i])
            print rssi_s
        else:
            break
            
rssi = int(rssi_s)
print rssi