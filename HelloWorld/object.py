class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")   # 移除头尾指定的字符（默认为空格）或字符序列
        msg = self.cooked_string + " " + msg + "."
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"

    def addCondiment(self, condiment):
        self.condiments.append(condiment)

# myDog = HotDog()
# print(myDog)
# print("Cooking hot dog for 4 minutes...")
# myDog.cook(4)
# print(myDog)
# print("Cooking hot dog for 3 minutes...")
# myDog.cook(3)
# print(myDog)
# print("What happens if I cook it for 10 more minutes?")
# myDog.cook(10)
# print(myDog)
# print("Now, I'm going to add some stuff on my hot dog")
# myDog.addCondiment("Ketchup")
# myDog.addCondiment("mustard")
# print(myDog)

# class Ball:     # 类
#     # 初始化
#     def __init__(self, color, size, direction):
#         self.color = color
#         self.size = size
#         self.direction = direction

#     def __str__(self):
#         msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
#         return msg

#     # 一个方法
#     def bounce(self):
#         if self.direction == 'down':
#             self.direction = 'up'

# # 设置一些属性
# myBall = Ball('red', 'small', 'down')

# # 打印对象的属性
# print('I just created a ball.')
# print('My ball is %s' % myBall.size)
# print("My ball's direction is %s" % myBall.direction)
# print("Now I'm going to bounce the Ball")
# print()
# myBall.bounce()     # 使用一个方法
# print("Now the ball's direction is %s" % myBall.direction)
# print(myBall)
