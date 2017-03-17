import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont


class MyWindow(QWidget):
    def __init__(self):
        # Creating app
        self.app = QApplication(sys.argv)
        super().__init__()
        # Start general window
        self.start_window()
        # Run application
        self.app.exec_()

    def start_window(self):
        # Creating font
        QToolTip.setFont(QFont('SansSerif', 10))
        # Prompt for widget
        self.setToolTip("This is widget")
        # Creating button
        self.button = QPushButton('Button', self)
        # Creating prompt for button
        self.button.setToolTip("Its button")
        # Button size
        self.button.resize(50, 50)
        # Button position
        self.button.move(30, 30)

        # Set window
        self.setGeometry(300, 300, 1400, 900)
        # Set win title
        self.setWindowTitle("Windows")
        # Set icon
        self.setWindowIcon(QIcon('picture/Samurai_smal.png'))

        # Show window
        self.show()


if __name__ == '__main__':
    MyWindow()
