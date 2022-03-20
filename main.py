from morse import morse_alphabet
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from Graphical import MyWidget
from PySide6.QtWidgets import QApplication, QPushButton


# print(morse_alphabet)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])


    widget = MyWidget()
    widget.resize(600, 300)
    widget.setStyleSheet("""
        border-color: #262626;
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        
   
    """)
    widget.show()




    sys.exit(app.exec())

