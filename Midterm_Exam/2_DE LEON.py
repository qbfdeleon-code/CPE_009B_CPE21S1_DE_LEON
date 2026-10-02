import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title= "Special Midterm Exam in OOP"
        self.x=200 # or left
        self.y=200 # or top
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click me to change color', self)
        self.button.setToolTip("Changes color when clicked")
        self.button.move(125, 30)  # button.move(x,y)
        self.button.clicked.connect(self.clickMe)
        
        self.show()

    @pyqtSlot()
    def clickMe(self):
        self.button.setStyleSheet("background-color: yellow; color: black;")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())


