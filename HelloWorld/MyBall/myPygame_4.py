import pygame
import random


# Ball 类的定义
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)         # 初始化动画精灵
        self.image = pygame.image.load(image_file)  # 在动画精灵中加载图像文件
        self.rect = self.image.get_rect()           # 得到定义图像边界的矩形
        self.rect.left, self.rect.top = location    # 设置球的初始位置
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        ball.move()         # 先移动所有的球
    for ball in group:
        group.remove(ball)  # 从动画精灵组中删除动画精灵
        # 检查动画精灵与动画精灵组之间的碰撞情况
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)     # 将球添加到原来的动画精灵组中
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()


# 初始化并画出沙滩球
size = width, height = 640, 480     # 设置窗口大小
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "b_ball_rect.png"
clock = pygame.time.Clock()         # 创建 Clock 类的实例
group = pygame.sprite.Group()       # 创建动画精灵组
for row in range(0, 2):
    for column in range(0, 2):
        # 每次循环时都有一个不同的位置
        location = [column * 180 + 10, row * 180 + 10]
        speed = [random.randint(-10, 10), random.randint(-10, 10)]
        ball = Ball(img_file, location, speed)     # 在这个位置上创建一个球
        group.add(ball)                            # 将每个球添加到动画精灵组中

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()            # 检查zhen速率
            print("frame rate =", frame_rate)
    animate(group)
    clock.tick(60)  # clock.tick() 函数现在控制了zhen速率（受计算机运行速度限制）
pygame.quit()
