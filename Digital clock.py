from stopwatch import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication , QLCDNumber
import sys,time

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Digital Clock -  Dynamic Coding')
        self.setGeometry(400,300,550,150)
        self.setWindowIcon(QtGui.QIcon('clock.png'))

        self.initUI()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.current_time)
        self.timer.start(1000)


    def initUI(self):
        self.clock_screen = QLCDNumber(self)
        self.clock_screen.setStyleSheet("color: black; background-color: white")
        self.clock_screen.setDigitCount(8)
        self.clock_screen.setGeometry(QtCore.QRect(0, 0, 550, 150))
        self.current_time()


    def current_time(self):
        current = time.strftime("%I:%M:%S")
        self.clock_screen.display(current)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())