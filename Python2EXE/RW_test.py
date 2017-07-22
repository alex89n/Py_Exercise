import time
import array
import os
import os.path
import shutil

def findNextDutToTest(dut):
    dutForTest = {}
    with open('d:\\_PM_TestList', 'r') as file:
        for line in file:        
            line = line.split(",")
            line[0] = int(line[0])
            dutForTest[line[0]] = line[1]
    for key in dutForTest:
        if  key > dut and dutForTest[key].find("True") != -1:
            return key
        
        
print findNextDutToTest(23)

    
    
    
    
    
    
        
# FILE_PATH="C:\\Users\\aleksandarn\\Desktop\\Python2EXE\\"
# with open(FILE_PATH + 'file.txt', 'r+') as file:
    # lines = file.readlines()
# print "lines:"
# print lines
# print ""

# PM_PANEL_TEST_FILE_TEMPLATE_PATH="d:\\ObloTB\\RTExecutor\\Templates\\"

# fileName = "C:\\Users\\aleksandarn\\Desktop\\Python2EXE\\run in shell\\AAAAAAA"
# shutil.copyfile( (PM_PANEL_TEST_FILE_TEMPLATE_PATH + 'TestFileTemplate_EXP_2SW.xls'), fileName)


# line = lines[len(lines)-1].split(' ')
# print "line:"
# print line
# print ""

# line = lines[0].split(' ')
# print line
# print ""

# panel_id = "%04d" % int(line[2])
# print panel_id

# ret = "RSSI:-38 LQI:120 DATA:01FFFFFFFFFFFFFFFF01060260"
# print "\n" + ret
# # print ret.find('RSSI', 0, 6) 

# # print ret.find('RSSI:')

# dataIndex = ret.find('RSSI:')
# rssi_s = ''
# if dataIndex != -1:
    # for i in range(0, 4):
        # if ret[dataIndex+len('RSSI:')+i] != ' ':
            # rssi_s += str(ret[dataIndex+len('RSSI:')+i])
            # # print  rssi_s
        # else:
            # break
    # print  rssi_s
    
# dataIndex = ret.find('DATA:')
# dutSN = ret[(dataIndex+7):(dataIndex+7+16)]
# devVersion = ret[(dataIndex+7+6):(dataIndex+7+6+2)]
# fwVersion = ret[(dataIndex+7+16+2):(dataIndex+7+16+2+6)]
# fwVersionFormated = fwVersion[0:2] + "." + fwVersion[2:4] + "." + fwVersion[4:6]
# print fwVersionFormated



# previousDut = int(line[1])
# print previousDut

 
# for line in lines[2:]:
    # line = line.split(',')
    # # Check if 
    # if ( int(line[0]) > 0 ) and ( line[1].find("True") != -1 ):
        # print int(line[0])
        # print ""
        # print line
        # print line[1].find("True") 
        # # print line[1].find("True")
        

# print "\nTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
# numberOfDUTs = 0
# print lines_1[2:]
# print "\nTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
# for line_1 in lines_1[2:]:
    # line_1 = line_1.split(',')
    # #print line_1
    # # Check if 
    # if ( line_1[1].find("True") != -1 ):
        # numberOfDUTs += 1
        # print numberOfDUTs