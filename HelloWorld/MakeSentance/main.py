import random
import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType("ms.ui")[0]


class MakeSentance(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btn_clicked(self):
        f1 = open("Adjective.txt", 'r')
        f2 = open("Noun.txt", "r")
        f3 = open("Verbphrase.txt", 'r')
        f4 = open("Adverbphrase.txt", 'r')
        self.adj = (random.choice(f1.readlines())).strip()
        self.n = (random.choice(f2.readlines())).strip()
        self.vp = (random.choice(f3.readlines())).strip()
        self.advp = (random.choice(f4.readlines())).strip()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        self.sentance.setText(
            f"The {self.adj} {self.n} {self.vp} {self.advp}.")

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
myapp = MakeSentance(None)
myapp.show()
app.exec_()
