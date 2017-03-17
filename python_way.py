import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont


class MyWindow(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.set_ui()
        self.app.exec_()

    def set_ui(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("This is widget")

        self.button = QPushButton('Button', self)
        self.button.setToolTip("Its button")
        self.button.resize(50, 50)
        self.button.move(30, 30)

        self.setGeometry(300, 300, 1400, 900)
        self.setWindowTitle("Windows")
        self.setWindowIcon(QIcon('picture/Samurai_smal.png'))

        self.show()


if __name__ == '__main__':
    MyWindow()
