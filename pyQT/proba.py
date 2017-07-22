# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
    
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)   
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('App')
        self.setWindowIcon(QIcon('icon.png'))
        self.center()
        self.setWindowTitle('Center') 

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip('This is a <b>Quit Button</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,150)
    
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit>", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()    
    sys.exit(app.exec_())

