import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.set_ui()
        self.app.exec_()

    def set_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Windows")
        self.setWindowIcon(QIcon('picture/Samurai_smal.png'))

        self.show()


if __name__ == '__main__':
    MyWindow()
