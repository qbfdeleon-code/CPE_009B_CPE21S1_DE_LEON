import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()  #initializes the main window like in the previous one
        self.title = "Midterm in OOP"
        self.left = 200
        self.top = 200
        self.w = 750
        self.h = 375
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.w, self.h)
        self.setWindowIcon(QIcon('pythonico.ico'))

        #Label
        self.label = QLabel('Enter your fullname:', self)
        self.label.setStyleSheet("color: red;")
        self.label.move(65, 125)

        #Textbox for typing the name
        self.textbox = QLineEdit(self)
        self.textbox.setFont(QFont("Arial", 16))
        self.textbox.setGeometry(375, 120, 310, 40)

        #Button
        self.button = QPushButton('Click to display your Fullname', self)
        self.button.setStyleSheet("color: red;")
        self.button.setGeometry(62, 185, 212, 33)
        self.button.clicked.connect(self.clickMe)

        #Second textbox that shows the result
        self.output = QLineEdit(self)
        self.output.setFont(QFont("Arial", 16))
        self.output.setGeometry(375, 183, 310, 40)
        self.output.setReadOnly(True)

        self.show()

    @pyqtSlot()
    def clickMe(self):
        self.output.setText(self.textbox.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())