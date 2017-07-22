import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog,
    QApplication, QFrame, QColorDialog, QSizePolicy, QFontDialog, QLabel,
    QVBoxLayout)
from PyQt5.QtGui import QColor

class Example(QWidget):
    """docstring for Example."""
    def __init__(self, arg):
        super(Example, self).__init__()
        self.arg = arg

        self.initUI()

    def initUI(self):

        # self.btn = QPushButton('Dialog', self)
        # self.btn.move(20,20)
        # self.btn.clicked.connect(self.showDialog)
        #
        # self.le = QLineEdit(self)
        # self.le.move(130,22)
        #
        # self.setGeometry(300, 300, 290, 150)
        # self.setWindowTitle('Input dialog')
        # self.show()

        # col = QColor(6, 5, 6)
        #
        # self.btn = QPushButton("Dialog", self)
        # self.btn.move(20, 20)
        #
        # self.btn.clicked.connect(self.showDialog)
        #
        # self.frm = QFrame(self)
        # self.frm = QFrame(self)
        # self.frm.setStyleSheet("QWidget { background-color: %s}" %col.name())
        # self.frm.setGeometry(130, 22, 100, 100)
        #
        # self.setGeometry(300, 300, 250, 180)
        # self.setWindowTitle("Color dialog")
        # self.show()

        vbox = QVBoxLayout()
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20,20)

        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowlege only masters', self)
        self.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Color dialog")
        self.show()

    def showDialog(self):
        # text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter you name:')
        # print(text)
        # print(ok)
        # if ok:
        #     self.le.setText(str(text))
        # else:
        #     self.le.setText("Something")

        # col = QColorDialog.getColor()
        # if col.isValid():
        #     self.frm.setStyleSheet("QWidget { background-color: %s}"
        #         %col.name())

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example("Alex")
    sys.exit(app.exec_())
