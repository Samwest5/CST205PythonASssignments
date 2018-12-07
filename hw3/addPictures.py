import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Manipulated Image'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        # Create widget
        label = QLabel()
        pixmap = QPixmap('image.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())