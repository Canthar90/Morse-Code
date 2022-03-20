import PySide6.QtCore
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from morse import morse_alphabet


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()



        self.edit = QtWidgets.QTextEdit("Write your sentence here", alignment=QtCore.Qt.AlignCenter)
        self.edit.setStyleSheet("""
        max-width: 350px;
        height: 150px; 
        """)

        edit = QtWidgets.QHBoxLayout()
        edit.addWidget(self.edit)



        self.button = QtWidgets.QPushButton("Morse it")
        self.button.setStyleSheet("""
        background-color: #D49B54;
        padding 20px;
        font-size: 18px;
        max-width: 120px;
        height: 50px;
        """)

        a = QtWidgets.QHBoxLayout()
        a.addWidget(self.button)


        self.text = QtWidgets.QTextEdit("......-...-..--- .-----.-..-..-..", alignment=QtCore.Qt.AlignCenter)
        self.text.setStyleSheet("""
        max-width: 350px;
        height: 150px;
        """)

        edit.addWidget(self.text)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addLayout(edit)



        self.layout.addLayout(a)

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
