import sys
from PyQt5 import QtWidgets, uic    # 导入需要的 PyQT 库

# 加载在 Qt Designer 中创建的用户界面
form_class = uic.loadUiType("MyFirstGui.ui")[0]


# 为主窗口定义一个类
class MyFirstWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # 将事件处理器与事件关联起来
        self.pushButton.clicked.connect(self.button_clicked)

    # 事件处理器
    def button_clicked(self):
        x = self.pushButton.x()
        y = self.pushButton.y()
        x += 50
        y += 50
        self.pushButton.move(x, y)


app = QtWidgets.QApplication(sys.argv)  # 运行事件循环的 PyQt 对象
myWindow = MyFirstWindow()              # 创建窗口类的实例
# 启动程序并显示 GUI 窗口
myWindow.show()
app.exec_()
