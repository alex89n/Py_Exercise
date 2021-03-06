import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog,
    QApplication)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    """docstring for Example."""
    def __init__(self, arg):
        super(Example,self).__init__()
        self.arg = arg

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('icon.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File dancing")
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/D:')
        print(fname)
        print(fname[0])

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText("Enter file: " + str(data))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example("Divlji")
    sys.exit(app.exec_())
