import pygame

# 初始化程序
pygame.init()
screen = pygame.display.set_mode([400, 600])
screen.fill([0, 0, 0])
ship = pygame.image.load('lunarlander.png')
moon = pygame.image.load('moonsurface.png')
ground = 540  # 降落点是 y = 540

start = 90
clock = pygame.time.Clock()
ship_mass = 5000.0      # 船的质量
fuel = 5000.0           # 燃料
velocity = -100.0       # 速度
gravity = 10            # 重力
height = 2000
thrust = 0              # 推力
delta_v = 0
y_pos = 90
held_down = False


# 反推发动机的 Sprite 类
class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([30, 10])    # 创建表面
        image_surface.fill([128, 128, 128])
        self.image = image_surface.convert()                # 将表面转换为图像
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location


# 计算高度、速度、加速度和燃料
def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    delta_t = 1 / fps   # “滴答”对应 Pygame 循环的一zhen
    # 将反推发动机精灵的 y 坐标转换为推力
    thrust = (500 - myThrottle.rect.centery) * 5.0
    fuel -= thrust / (10 * fps)     # 根据推力减少燃料
    if fuel < 0:
        fuel = 0.0
    if fuel < 0.1:
        thrust = 0.0
    # 物理公式
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel))
    velocity = velocity + delta_v
    delta_h = velocity * delta_t
    height = height + delta_h
    # 将高度转换为 Pygame 的 y 坐标
    y_pos = ground - (height * (ground - start) / 2000) - 90


# 使用字体对象显示统计信息
def display_stats():
    v_str = f"velocity: {velocity:.2f} m/s"
    h_str = f"height:   {height:.2f}"
    t_str = f"thrust:   {thrust:.2f}"
    a_str = f"acceleration: {(delta_v * fps):.2f}"
    f_str = f"fuel:  {fuel:.2f}"
    v_font = pygame.font.Font(None, 26)
    v_surf = v_font.render(v_str, 1, (255, 255, 255))
    screen.blit(v_surf, [10, 50])
    a_font = pygame.font.Font(None, 26)
    a_surf = a_font.render(a_str, 1, (255, 255, 255))
    screen.blit(a_surf, [10, 100])
    h_font = pygame.font.Font(None, 26)
    h_surf = h_font.render(h_str, 1, (255, 255, 255))
    screen.blit(h_surf, [10, 150])
    t_font = pygame.font.Font(None, 26)
    t_surf = t_font.render(t_str, 1, (255, 255, 255))
    screen.blit(t_surf, [10, 200])
    f_font = pygame.font.Font(None, 26)
    f_surf = f_font.render(f_str, 1, (255, 255, 255))
    screen.blit(f_surf, [60, 300])


# 画出尾焰三角形
def display_flames():
    flame_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        # 使用两个三角形显示火箭尾焰
        pygame.draw.polygon(screen, [255, 109, 14], [(startx, starty),
                            (startx + 4, starty + flame_size), (startx + 8, starty)], 0)


# 当游戏结束时显示最终统计信息
def display_final():
    final1 = "Game over"
    final2 = f"You landed at {velocity:.2f} m/s"
    if velocity > -5:
        final3 = "Nice landing!"
        final4 = "I hear NASA is hiring!"
    elif velocity > -15:
        final3 = "Ouch! A bit rough, but you survived."
        final4 = "You'll do better next time."
    else:
        final3 = "Yikes! You crashed a 30 Billion dollar ship."
        final4 = "How are you getting home?"
    pygame.draw.rect(screen, [0, 0, 0], [5, 5, 350, 280], 0)
    f1_font = pygame.font.Font(None, 70)
    f1_surf = f1_font.render(final1, 1, (255, 255, 255))
    screen.blit(f1_surf, [20, 50])
    f2_font = pygame.font.Font(None, 40)
    f2_surf = f2_font.render(final2, 1, (255, 255, 255))
    screen.blit(f2_surf, [20, 110])
    f3_font = pygame.font.Font(None, 26)
    f3_surf = f3_font.render(final3, 1, (255, 255, 255))
    screen.blit(f3_surf, [20, 150])
    f4_font = pygame.font.Font(None, 26)
    f4_surf = f4_font.render(final4, 1, (255, 255, 255))
    screen.blit(f4_surf, [20, 180])
    pygame.display.flip()


myThrottle = ThrottleClass([15, 500])
running = True
while running:
    clock.tick(30)
    fps = clock.get_fps()
    if fps < 1:
        fps = 30
    if height > 0.01:
        calculate_velocity()
        screen.fill([0, 0, 0])
        display_stats()
        # 画出燃料表轮廓
        pygame.draw.rect(screen, [0, 0, 255], [80, 350, 24, 100], 2)
        fuelbar = 96 * fuel / 5000
        # 燃料量
        pygame.draw.rect(screen, [0, 255, 0],
                         [84, 448 - fuelbar, 18, fuelbar], 0)
        # 画出反推发动机滑块
        pygame.draw.rect(screen, [255, 0, 0], [25, 300, 10, 200], 0)
        # 画出月球
        screen.blit(moon, [0, 500, 400, 100])
        # 着陆点
        pygame.draw.rect(screen, [60, 60, 60], [220, 535, 70, 5], 0)
        # 画出推力操作杆
        screen.blit(myThrottle.image, myThrottle.rect)
        display_flames()
        # 画出飞船
        screen.blit(ship, [230, y_pos, 50, 90])
        instruct1 = "Land softly without running out of fuel"
        instruct2 = "Good landing: < 15m/s Great landing: < 5m/s"
        inst1_font = pygame.font.Font(None, 24)
        inst1_surf = inst1_font.render(instruct1, 1, [255, 255, 255])
        screen.blit(inst1_surf, [50, 550])
        inst2_font = pygame.font.Font(None, 24)
        inst2_surf = inst2_font.render(instruct2, 1, [255, 255, 255])
        screen.blit(inst2_surf, [20, 575])
        pygame.display.flip()

    else:
        # 游戏结束——打印最终得分
        display_final()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 检测鼠标是否反推发动机
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION:
            if held_down:
                # 更新反推发动机位置
                myThrottle.rect.centery = event.pos[1]  # [1]表示鼠标 Y 坐标
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500
pygame.quit()
