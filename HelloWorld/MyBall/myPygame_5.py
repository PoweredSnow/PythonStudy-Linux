import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


my_ball = Ball('beach_ball.png', [10, 0], [20, 20])
pygame.time.set_timer(pygame.USEREVENT, 1000)   # 创建定时器
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)
held_down = False
direction = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 检查按键，让球上移或下移
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.rect.top = my_ball.rect.top - 10
            elif event.key == pygame.K_DOWN:
                my_ball.rect.top = my_ball.rect.top + 10
        # 检查鼠标左键是否处于按下状态
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        # 检测鼠标移动事件并移动沙滩球
        elif event.type == pygame.MOUSEMOTION:
            # 拖拽鼠标时执行该操作
            if held_down:
                my_ball.rect.center = event.pos
        # 定时器的事件处理器
        elif event.type == pygame.USEREVENT:
            my_ball.rect.centery = my_ball.rect.centery + (30 * direction)
            if my_ball.rect.top <= 0 or \
                    my_ball.rect.bottom >= screen.get_rect().bottom:
                direction = -direction
    clock.tick(60)
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
pygame.quit()
