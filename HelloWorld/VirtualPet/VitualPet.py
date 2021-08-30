import sys
import pickle
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets, uic

formclass = uic.loadUiType("VirtualPet.ui")[0]


class VirtualPetWindow(QtWidgets.QMainWindow, formclass):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # 初始化
        self.doctor = False
        self.walking = False
        self.sleeping = False
        self.playing = False
        self.eating = False
        self.time_cycle = 0
        self.hunger = 0
        self.happiness = 8
        self.health = 8
        self.forceAwake = False
        # 用于动画的图像列表
        self.sleepImages = ["sleep1.gif", "sleep2.gif", "sleep3.gif",
                            "sleep4.gif"]
        self.eatImages = ["eat1.gif", "eat2.gif"]
        self.walkImages = ["walk1.gif", "walk2.gif", "walk3.gif",
                           "walk4.gif"]
        self.playImages = ["play1.gif", "play2.gif"]
        self.doctorImages = ["doc1.gif", "doc2.gif"]
        self.nothingImages = ["pet1.gif", "pet2.gif", "pet3.gif"]

        self.imageList = self.nothingImages
        self.imageIndex = 0

        # 将事件处理器连接到工具栏按钮
        self.actionStop.triggered.connect(self.stop_Click)
        self.actionFeed.triggered.connect(self.feed_Click)
        self.actionWalk.triggered.connect(self.walk_Click)
        self.actionPlay.triggered.connect(self.play_Click)
        self.actionDoctor.triggered.connect(self.doctor_Click)

        # 设置定时器
        self.myTimer1 = QtCore.QTimer(self)
        self.myTimer1.start(500)
        self.myTimer1.timeout.connect(self.animation_timer)
        self.myTimer2 = QtCore.QTimer(self)
        self.myTimer2.start(5000)
        self.myTimer2.timeout.connect(self.tick_timer)

        # 尝试打开 pickle 文件
        filehandle = True
        try:
            file = open("savedata_vp.pkl", "rb")
        except:
            filehandle = False
        if filehandle:
            # 如果可以打开，则读取该文件
            save_list = pickle.load(file)
            file.close()
        else:
            # 如果没有打开，则使用默认值
            save_list = [8, 8, 0, datetime.datetime.now(), 0]
        # 从列表中取出单个值
        self.happiness = save_list[0]
        self.health = save_list[1]
        self.hunger = save_list[2]
        timestamp_then = save_list[3]
        self.time_cycle = save_list[4]

        # 检查自最后一次运行以来经过了多长时间
        difference = datetime.datetime.now() - timestamp_then
        ticks = int(difference.seconds / 50)
        for i in range(ticks):
            # 模拟程序关闭期间发生的所有嘀嗒
            self.time_cycle += 1
            if self.time_cycle == 60:
                self.time_cycle = 0
            # 醒着
            if self.time_cycle < 48:
                self.sleeping = False
            if self.hunger < 8:
                self.hunger += 1
            else:
                self.sleeping = True
                if self.hunger < 8 and self.time_cycle % 3 == 0:
                    self.hunger += 1
            if self.hunger == 7 and (self.time_cycle % 2 == 0) \
                    and self.health > 0:
                self.health -= 1
            if self.hunger == 8 and self.health > 0:
                self.health -= 1
        # 使用正确的动画——醒着或睡觉
        if self.sleeping:
            self.imageList = self.sleepImages
        else:
            self.imageList = self.nothingImages

    # 执行动作之前检查宠物是否正在睡觉
    def sleep_test(self):
        if self.sleeping:
            result = (QtWidgets.QMessageBox.warning(self, "WARNING", "Are you sure you want to wake your pet up? He'll be unhappy about it!", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No))

            if result == QtWidgets.QMessageBox.Yes:
                self.sleeping = False
                self.happiness -= 4
                self.forceAwake = True
                return True
            else:
                return False
        else:
            return True

    # 医生按钮事件处理器
    def doctor_Click(self):
        if self.sleep_test():
            self.imageList = self.doctorImages
            self.doctor = True
            self.walking = False
            self.eating = False
            self.playing = False

    # 喂食按钮事件处理器
    def feed_Click(self):
        if self.sleep_test():
            self.imageList = self.eatImages
            self.eating = True
            self.walking = False
            self.playing = False
            self.doctor = False

    # 玩耍按钮事件处理器
    def play_Click(self):
        if self.sleep_test():
            self.imageList = self.playImages
            self.playing = True
            self.walking = False
            self.eating = False
            self.doctor = False

    # 散步按钮事件处理器
    def walk_Click(self):
        if self.sleep_test():
            self.imageList = self.walkImages
            self.walking = True
            self.eating = False
            self.playing = False
            self.doctor = False

    # 停止按钮事件处理器
    def stop_Click(self):
        if self.sleep_test():
            self.imageList = self.nothingImages
            self.walking = False
            self.eating = False
            self.playing = False
            self.doctor = False

    # 动画定时器（每0.5秒）事件处理器
    def animation_timer(self):
        if self.sleeping and not self.forceAwake:
            self.imageList = self.sleepImages
        self.imageIndex += 1
        if self.imageIndex >= len(self.imageList):
            self.imageIndex = 0
        icon = QtGui.QIcon()
        # 更新宠物的图像（动画）
        current_image = self.imageList[self.imageIndex]
        icon.addPixmap(QtGui.QPixmap(current_image),
                       QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.petPic.setIcon(icon)
        self.progressBar_1.setProperty("value", (8-self.hunger)*(100/8.0))
        self.progressBar_2.setProperty("value", self.happiness*(100/8.0))
        self.progressBar_3.setProperty("value", self.health*(100/8.0))

    # 5秒定时器事件处理器从这里开始
    def tick_timer(self):
        # 检查是睡觉还是醒着
        self.time_cycle += 1
        if self.time_cycle == 60:
            self.time_cycle = 0
        if self.time_cycle <= 48 or self.forceAwake:
            self.sleeping = False
        else:
            self.sleeping = True
        if self.time_cycle == 0:
            self.forceAwake = False
        # 根据活动量增加或减少单位
        if self.doctor:
            self.health += 1
            self.hunger += 1
        elif self.walking and (self.time_cycle % 2 == 0):
            self.happiness += 1
            self.health += 1
            self.hunger += 1
        elif self.playing:
            self.happiness += 1
            self.hunger += 1
        elif self.eating:
            self.hunger -= 2
        elif self.sleeping:
            if self.time_cycle % 3 == 0:
                self.hunger += 1
        else:
            self.hunger += 1
            if self.time_cycle % 2 == 0:
                self.happiness -= 1
        # 确保值没有超出范围
        if self.hunger > 8:
            self.hunger = 8
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger == 7 and (self.time_cycle % 2 == 0):
            self.health -= 1
        if self.hunger == 8:
            self.health -= 1
        if self.health > 8:
            self.health = 8
        if self.health < 0:
            self.health = 0
        if self.happiness > 8:
            self.happiness = 8
        if self.happiness < 0:
            self.happiness = 0
        # 更新进度条
        self.progressBar_1.setProperty("value", (8-self.hunger)*(100/8.0))
        self.progressBar_2.setProperty("value", self.happiness*(100/8.0))
        self.progressBar_3.setProperty("value", self.health*(100/8.0))

    def closeEvent(self, event):
        file = open("savedata_vp.pkl", "wb")
        save_list = [self.happiness, self.health, self.hunger,
                     datetime.datetime.now(), self.time_cycle]
        pickle.dump(save_list, file)
        event.accept()

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
myapp = VirtualPetWindow()
myapp.show()
app.exec_()
