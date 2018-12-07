# Sam Westigard
# Homework 3
# CST 205
# contains gui classes, calls search function

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from search import bestMatch
from PIL import Image





options = ['Select Manipulation', 'Sepia', 'Negative', 'Grayscale', 'Thumbnail', 'none']


def makeSepia(p):

    if p[0] < 63:
        r, g, b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
    elif p[0] > 62 and p[0] < 192:
        r, g, b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)

    else:
        r = int(p[0] * 1.08)
        if r > 255:
            r = 255
        g, b = p[1], int(p[2] * 0.5)
    return r, g, b

def sepia(id):
    im = Image.open('images/' + id + '.jpg')
    sepiaList = [makeSepia(p) for p in im.getdata()]
    im.putdata(list(sepiaList))
    im.save('manipulated.jpg')

def negative(id):
    im = Image.open('images/' + id + '.jpg')
    negativeList = [(255 - p[0], 255 - p[1], 255 - p[2]) for p in im.getdata()]
    im.putdata(list(negativeList))
    im.save('manipulated.jpg')

def grayscale(id):
    im = Image.open('images/' + id + '.jpg')
    new_list = map(lambda a: (int((a[0] + a[1] + a[2]) / 3),) * 3, im.getdata())
    im.putdata(list(new_list))
    im.save('manipulated.jpg')

def thumbnail(id):
    im = Image.open('images/' + id + '.jpg')
    im2 = im.copy()
    im2.thumbnail((im.height // 2, im.width // 2))
    im2.save('manipulated.jpg')

def none(id):
    im = Image.open('images/' + id + '.jpg')
    im.save('manipulated.jpg')


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image")
        label = QLabel(self)
        pixmap = QPixmap('manipulated.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

class ImageManipulationGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.search = QLabel("Enter Search Tags: ")
        self.searchField = QLineEdit("")
        searchBox = QHBoxLayout()
        searchBox.addWidget(self.search)
        searchBox.addWidget(self.searchField)

        self.imageEffect = QComboBox()
        self.imageEffect.addItems(options)
        optionsBox = QHBoxLayout()
        optionsBox.addWidget(self.imageEffect)

        self.readyButton = QPushButton("Click when ready", self)
        readyBox = QVBoxLayout()
        readyBox.addWidget(self.readyButton)
        self.readyButton.clicked.connect(self.readyClick)

        gbox1 = QGroupBox()
        gbox1.setLayout(searchBox)

        gbox2 = QGroupBox()
        gbox2.setLayout(optionsBox)

        gbox3 = QGroupBox()
        gbox3.setLayout(readyBox)

        mbox1 = QVBoxLayout()
        mbox1.addWidget(gbox1)
        mbox1.addWidget(gbox2)
        mbox1.addWidget(gbox3)

        self.setLayout(mbox1)
        self.setWindowTitle('Image Manipulator')

    @pyqtSlot()
    def readyClick(self):
        # TODO filter input
        self.searchTags = self.searchField.text().split()
        self.searchTags = set([x.lower() for x in self.searchTags])
        self.bestMatchID = bestMatch(self.searchTags)

        choiceIndex = self.imageEffect.currentIndex()
        self.choice = options[choiceIndex]

        if(self.choice == 'Sepia'):
            sepia(self.bestMatchID)

        elif(self.choice == 'Negative'):
            negative(self.bestMatchID)

        elif(self.choice == 'Grayscale'):
            grayscale(self.bestMatchID)

        elif(self.choice == 'Thumbnail'):
            thumbnail(self.bestMatchID)

        else:
            none(self.bestMatchID)

        self.imageWindow = ImageWindow()
        self.imageWindow.show()



app = QApplication(sys.argv)
main = ImageManipulationGUI()
main.show()
sys.exit(app.exec_())








