import time
import subprocess
from subprocess import check_output
import array
import os
import os.path
import threading
import sys

# Path to SmartRFProgrammer console application
PROGRAMMER_APP_PATH = "c:\\Progra~2\\Texasi~1\\SmartR~1\\FlashP~1\\bin\\SmartRFProgConsole.exe"
# PARAMETERS = " S EP F=\"SO10M1-ZB-C4_4.2.1_4577_20170616.hex\""
PARAMETERS = " S EPVC F=\"BLEplug_20_11_15-133.hex\""

PROGRAMMER_DETECT_DUT_APP_PATH = "c:\\Progra~2\\Texasi~1\\SmartR~1\\FlashP~1\\bin\\sw_redetect.exe"
PROGRAMMER_ERASE_DUT_PATH = "c:\\Progra~2\\Texasi~1\\SmartR~1\\FlashP~1\\bin\\SmartRFProgConsole.exe S CE"

PROGRAMMER_READ_IEEE_ADDR = "c:\\Progra~2\\Texasi~1\\SmartR~1\\FlashP~1\\bin\\SmartRFProgConsole.exe S RI(F=0, SEC)"

def buildCommand():
    # Build programming command
    # Write generated serial number to specific flash location of PM's CC2530 mcu
    # cmdStr = PROGRAMMER_APP_PATH + PARAMETERS + " WI(F=0,I=" + serialNum + ")" + " LPD(0-118)"
    cmdStr = PROGRAMMER_APP_PATH + PARAMETERS # + " LP(0-119)"
    return cmdStr

def printProgressBar (iteration, total, prefix = 'Progress: ' ,
    suffix = 'Complete', decimals = 1, length = 45, fill = '#'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total:
        print()

def statusBar():
        i = 1
        l = 30
        # sys.stdout.write("Progress: |")
        for i in range(l+1):
            # sys.stdout.write("#")
            # sys.stdout.flush()
            printProgressBar(i, l)
            time.sleep(0.1)
        # sys.stdout.write("| 100% Complete\n")

def main():

    os.system('cls')

    command = buildCommand()

    subprocess.Popen(PROGRAMMER_DETECT_DUT_APP_PATH, stdout=subprocess.PIPE, shell=True)
    time.sleep(0.5)

    subprocess.Popen(PROGRAMMER_ERASE_DUT_PATH, stdout=subprocess.PIPE, shell=True)
    time.sleep(0.5)

    # read IEEE address
    proc = subprocess.Popen(PROGRAMMER_READ_IEEE_ADDR, stdout=subprocess.PIPE, shell=True)
    # out = check_output(PROGRAMMER_READ_IEEE_ADDR) #, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    if out.find("IEEE address:") < 0:
        IEEE_Addr = "\nNO IEEE Address"
        print(IEEE_Addr)

    else:
        IEEE_Addr = out[out.find("IEEE address:") + 14:]
        print("\nRead IEEE Address: \n" + str(IEEE_Addr))
        with open("C4_Outlet_MAC_List.txt", 'a') as f:
            f.write(str(IEEE_Addr) + "\n")

        print("\nStart burning...")
        status = threading.Thread(name = "statusBar", target = statusBar)
        status.start()

    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    # If programming failed, try once more time
    if (out.find("Erase, program and verify (CRC) OK") < 0):
        subprocess.Popen(PROGRAMMER_DETECT_DUT_APP_PATH, stdout=subprocess.PIPE, shell=True)
        time.sleep(0.5)

        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()


    # Check programmer app output string for status
    if (out.find("Erase, program and verify (CRC) OK") >= 0 and  IEEE_Addr != "NO IEEE Address" ):
        print("\nErase, program and verify (CRC) OK")
        print("Programming PASS")

    else:
        print(out)
        print("\nProgramming FAIL" )

    user = raw_input("\nPress Enter to continue... (Enter Q for Quit)")
    if user == 'q':
        return False
    else:
        return True


if __name__ == "__main__":

    # main()
    loop = True
    while loop:
        loop = main()
