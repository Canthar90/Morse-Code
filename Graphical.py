import PySide6.QtCore
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from morse import morse_alphabet


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.edit = QtWidgets.QLineEdit("Write your sentence here", alignment=QtCore.Qt.AlignCenter)


        self.button = QtWidgets.QPushButton("Morse it"
                                            )
        self.text = QtWidgets.QLineEdit("......-...-..--- .-----.-..-..-..", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.morse_it)

    @QtCore.Slot()
    def morse_it(self):
        text = self.edit.text().lower()
        listed = list(text)
        morsed=''
        # print(f'{listed}')
        for element in listed:
            morsed += morse_alphabet[element]


        self.text.setText(morsed)
