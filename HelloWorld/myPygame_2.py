# import pygame
# pygame.init()

# dots = [[221, 432], [225, 331], [133, 342], [141, 310],
#         [51, 230], [74, 217], [58, 153], [114, 164],
#         [123, 135], [176, 190], [159, 77], [193, 93],
#         [230, 28], [267, 93], [301, 77], [284, 190],
#         [327, 135], [336, 164], [402, 153], [386, 217],
#         [409, 230], [319, 310], [327, 342], [233, 331],
#         [237, 432]]

# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# pygame.draw.lines(screen, [0, 0, 255], True, dots, 2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 用大量很小的矩形画出正弦曲线
import pygame
import sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
# plotPoints = []   # 2.
for x in range(0, 640):     # 从左到右循环
    # 计算每个点的y坐标（垂直坐标）
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)
    # 2.plotPoints.append([x, y])   # 将所有点添加到列表中
    # 3.逐点绘制
    screen.set_at([x, y], [0, 0, 0])
    # 1.使用小矩形来画点
    # pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)
# 2.用 draw.lines()方法画出整条曲线
# pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 2)
# 3.使用 surface.get_at() 方法查看像素点的颜色
print(screen.get_at([320, 240]))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
