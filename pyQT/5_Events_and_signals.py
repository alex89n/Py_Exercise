import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout,
    QApplication, QPushButton, QMainWindow)

class Communicate(QObject):
    closeApp = pyqtSignal()


# class Example(QWidget):
class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)
        #
        # self.setLayout(vbox)
        # sld.valueChanged.connect(lcd.display)
        #
        # self.setGeometry(300, 300, 250, 150)
        # self.setWindowTitle("Signal & slot")
        # self.show()


        # btn1 = QPushButton("Button 1", self)
        # btn1.move(30, 50)
        #
        # btn2 = QPushButton("Button 2", self)
        # btn2.move(150, 50)
        #
        # btn1.clicked.connect(self.buttonClicked)
        # btn2.clicked.connect(self.buttonClicked)
        #
        # self.statusBar()
        #
        # self.setGeometry(300, 300, 290, 150)
        # self.setWindowTitle('Event sender')
        # self.show()

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
