 # pyuic5 -x firstgui.ui -o firstgui.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sp_prog_gui import Ui_Dialog

import subprocess

PROGRAMMER_READ_IEEE_ADDR = "c:\\Progra~2\\Texasi~1\\SmartR~1\\FlashP~1\\bin\\SmartRFProgConsole.exe S RI(F=0, SEC)"

class SmartPlugProgramer(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.pushButton.clicked.connect(self.readIEEE)

    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)
        
    def readIEEE(self):   
        
        proc = subprocess.Popen(PROGRAMMER_READ_IEEE_ADDR, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        out = str(out)
        
        if out.find("IEEE address:") < 0:
            IEEE_Addr = "\nNO IEEE Address"
            print(out)
            print(IEEE_Addr)            
            return IEEE_Addr           

        else:
            IEEE_Addr = out[out.find("IEEE address:") + 14:]
            print("\nRead IEEE Address: \n" + str(IEEE_Addr))
            return IEEE_Addr
            
            
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = SmartPlugProgramer(dialog)

    dialog.show()
    sys.exit(app.exec_())