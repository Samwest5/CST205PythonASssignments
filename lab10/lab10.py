import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot

my_list = ["Pick A Color", "Black", "White", "Blue", "Red"]

theD = {'Pick A Color': '0', 'Black': '(0,0,0) #000000', 'White': '(255,255,255) #FFFFFF',
        'Blue': '(0,0,225) #0000FF', 'Red': '(255,0,0) #FF0000'}




class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,200)

        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_list)
        self.my_label = QLabel("")


        vbox = QVBoxLayout()
        vbox.addWidget(self.my_combo_box)
        vbox.addWidget(self.my_label)

        self.setLayout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)
        self.setWindowTitle("RGB and Hex")

    @pyqtSlot()
    def update_ui(self):
        my_text = self.my_combo_box.currentText()
        my_index = self.my_combo_box.currentIndex()
        self.my_label.setText(f'You chose {my_list[my_index]}.')
        self.my_label.setText(f'RGB and Hex values are {theD[my_list[my_index]]}')

print(theD)

app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())