import pygame
pygame.init()


screen = pygame.display.set_mode([640, 480])
pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.30)         # 调节音乐的音量
pygame.mixer.music.play()
splat = pygame.mixer.Sound("splat.wav")     # 创建声音对象
splat.set_volume(0.50)                      # 调节音效的音量
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 检查歌曲是否播放完毕
    if not pygame.mixer.music.get_busy():
        splat.play()
        # 等待1秒让“啪”声结束
        pygame.time.delay(1000)
        running = False
pygame.quit()
