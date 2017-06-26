import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    """docstring for Example."""
    def __init__(self, arg):
        super(Example, self).__init__()
        self.arg = arg

        self.initUI()

    def initUI(self):

        cb = QCheckBox("Show title", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("Checked")
        else:
            self.setWindowTitle(" ")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example("Divlji")
    sys.exit(app.exec_())
