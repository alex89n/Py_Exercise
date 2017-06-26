import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel, QLineEdit, QTextEdit

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

        # grid = QGridLayout()
        # self.setLayout(grid)
        #
        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #         '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #         '0', '.', '=', '+']
        #
        # position = [(i,j) for i in range(5) for j in range(4)]
        #
        # for position, name in zip(position, names):
        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)
        #
        # self.move(300,150)
        # self.setWindowTitle("Calculator")
        # self.show()


        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")
        #
        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)
        #
        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)
        #
        # self.setLayout(vbox)
        #
        # self.setGeometry(300, 300, 300, 150)
        # self.setWindowTitle('Absolute')
        # self.show()kup

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
