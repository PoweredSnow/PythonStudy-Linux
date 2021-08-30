import sys
from PyQt5 import QtWidgets, uic
import random

form_class = uic.loadUiType("myHangman.ui")[0]


# 查找字母
def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations


# 当玩家猜对字母时，用字母替换横线
def replace_letters(string, locations, letter):
    new_string = ''
    for i in range(0, len(string)):
        if i in locations:
            new_string = new_string + letter
        else:
            new_string = new_string + string[i]
    return new_string


# 当程序开始时，用横线替换相应的字母
def dashes(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_string = ''
    for i in word:
        if i in letters:
            new_string += "-"
        else:
            new_string += i
    return new_string


class HangmanGame(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # 连接事件处理器
        self.btn_guess.clicked.connect(self.btn_guess_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
        # 游戏角色部分
        self.pieces = [self.head, self.body, self.leftarm, self.leftleg,
                       self.rightarm, self.rightleg]
        # 绞刑架部分
        self.gallows = [self.line1, self.line2, self.line3, self.line4]
        self.pieces_shown = 0
        self.currentword = ""
        # 得到词汇表
        f = open("words.txt", 'r')
        self.lines = f.readlines()
        f.close()
        self.new_game()

    def new_game(self):
        self.guesses.setText("")
        # 从词汇表中随机选择一个单词
        self.currentword = random.choice(self.lines)
        self.currentword = self.currentword.strip()
        # 隐藏游戏角色
        for i in self.pieces:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
            i.setHidden(True)
        for i in self.gallows:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
        # 调用函数，用横线替换字母
        self.word.setText(dashes(self.currentword))
        self.pieces_shown = 0

    def btn_guess_clicked(self):
        # 让玩家猜字母或单词
        guess = str(self.guessBox.text())
        if str(self.guesses.text()) != "":
            self.guesses.setText(str(self.guesses.text()) + ", " + guess)
        else:
            self.guesses.setText(guess)
        # 猜字母
        if len(guess) == 1:
            if guess in self.currentword:
                locations = find_letters(guess, self.currentword)
                self.word.setText(str(replace_letters(self.word.text(),
                                                      locations, guess)))
                if str(self.word.text()) == self.currentword:
                    self.win()
            else:
                self.wrong()
        # 猜单词
        else:
            if guess == self.currentword:
                self.win()
            else:
                self.wrong()
        self.guessBox.setText("")

    # 当玩家猜对时，显示对话框
    def win(self):
        QtWidgets.QMessageBox.information(self, "Hangman", "You win!")
        self.new_game()

    # 猜错的情况
    def wrong(self):
        self.pieces_shown += 1
        # 显示游戏角色的另一部分
        for i in range(self.pieces_shown):
            self.pieces[i].setHidden(False)
        if self.pieces_shown == len(self.pieces):
            # 玩家输了
            message = "You lose. The word was " + self.currentword
            QtWidgets.QMessageBox.warning(self, "Hangman", message)
            self.new_game()

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
myapp = HangmanGame(None)
myapp.show()
app.exec_()
