import sys
from PyQt5 import QtWidgets, uic

form_class = uic.loadUiType("tempconv.ui")[0]


class TemperatureConverterWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnCtoF.clicked.connect(self.btnCtoF_clicked)
        self.btnFtoC.clicked.connect(self.btnFtoC_clicked)
        self.actionC_to_F.triggered.connect(self.btnCtoF_clicked)
        self.actionF_to_C.triggered.connect(self.btnFtoC_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)

    def btnCtoF_clicked(self):
        cel = float(self.editCel.text())    # 获取摄氏度
        fahr = cel * 9 / 5 + 32             # 转换为华氏度
        # 四舍五入并放入华氏度的 Spin Box 组件
        self.spinFahr.setValue(int(fahr + 0.5))

    def btnFtoC_clicked(self):
        fahr = self.spinFahr.value()
        cel = (fahr - 32) * 5 / 9
        self.editCel.setText(str("%.2f" % cel))

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
myWindow = TemperatureConverterWindow(None)
myWindow.show()
app.exec_()
