import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score, score_font, score_surf
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            if self.speed[1] > 0:
                self.speed[1] += 0.1
            if self.speed[1] < 0:
                self.speed[1] -= 0.1
            hit_wall.play()

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            if self.speed[0] > 0:
                self.speed[0] += 0.1
            if self.speed[0] < 0:
                self.speed[0] -= 0.1
            score = score + 1
            score_surf = score_font.render(str(score), 1, (0, 0, 0))
            get_point.play()


class Paddle(pygame.sprite.Sprite):
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])   # 为球拍创建表面
        image_surface.fill([0, 0, 0])           # 用黑色填充这个表面
        self.image = image_surface.convert()    # 将这个表面转换为图像
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# 初始化
pygame.init()
pygame.mixer.init()

# 背景音乐
pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
# 音效
hit = pygame.mixer.Sound("hit_paddle.wav")
hit.set_volume(0.4)
hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)
get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.2)
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.6)
new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)
bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.6)

screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [random.randint(3, 7) + random.random(),
              random.randint(1, 5) + random.random()]
myBall = Ball('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = Paddle([270, 400])
lives = 3
score = 0

score_font = pygame.font.Font(None, 50)     # 创建字体对象
# 渲染文本到 score_surf 表面
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = [10, 10]
done = False

# 主程序
running = True
while running:
    clock.tick(60)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 检测鼠标运动，移动球拍
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]  # [0]表示鼠标 X 坐标
    # 检测球与球拍之间的碰撞
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]
        if myBall.speed[0] > 0:
            myBall.speed[0] += 0.1
        if myBall.speed[0] < 0:
            myBall.speed[0] -= 0.1
        hit.play()

    myBall.move()   # 移动球

    if not done:
        # 重绘屏幕
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)  # 把含有分数文本的表面块移到这个位置
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(myBall.image, (width - 40 * i, 20))
        pygame.display.flip()

    # 如果球碰到底边就减一条命
    if myBall.rect.top >= screen.get_rect().bottom:
        if not done:
            splat.play()
        lives = lives - 1
        # 创建和绘制最终的分数文本
        if lives <= 0:
            if not done:
                pygame.time.delay(1000)
                bye.play()
            pygame.time.delay(1000)
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, [0, 0, 0])
            screen.blit(ft1_surf, [screen.get_width() // 2 -
                        ft1_surf.get_width() // 2, 100])
            screen.blit(ft2_surf, [screen.get_width() // 2 -
                        ft2_surf.get_width() // 2, 200])
            pygame.display.flip()
            done = True
            myBall.speed = [0, 0]
            pygame.mixer.music.fadeout(2000)
        else:
            # 2秒之后，获得新的一条命，重新开始
            pygame.time.delay(1000)
            new_life.play()
            myBall.rect.topleft = [(screen.get_rect().width) - 40 * lives, 20]
            myBall.speed = [random.randint(3, 7) + random.random(),
                            random.randint(1, 5) + random.random()]
            pygame.time.delay(1000)
pygame.quit()
