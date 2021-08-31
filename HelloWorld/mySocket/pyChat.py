import pygame
import socket

pygame.init()
screen_width, screen_height = screen_size = (640, 320)
font = pygame.font.Font(None, 50)
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
space_character_width = 8
message_spacing = 8
connection = socket.create_connection(('localhost', 12345))
connection.setblocking(False)
screen = pygame.display.set_mode(screen_size)
pygame.key.set_repeat(300, 100)


def message_to_surface(message):
    words = message.split(' ')
    word_surfs = []
    word_locations = []
    word_x = 0
    word_y = 0
    text_height = 0
    for word in words:
        # 创建一个表面,只包含一个单词
        word_surf = font.render(word, True, text_color, bg_color)
        # 单词超过屏幕时折行
        if word_x + word_surf.get_width() > screen_width:
            word_x = 0
            word_y = text_height
        word_surfs.append(word_surf)
        word_locations.append((word_x, word_y))
        # 在单词间加入空格
        word_x += word_surf.get_width() + space_character_width
        if word_y + word_surf.get_height() > text_height:
            text_height = word_y + word_surf.get_height()
    # 将所有单词表面绘制到一个大表面上
    surf = pygame.Surface((screen_width, text_height))
    surf.fill(bg_color)
    for i in range(len(words)):
        surf.blit(word_surfs[i], word_locations[i])
    return surf


message_surfs = []


def add_message(message):
    if len(message_surfs) > 50:
        message_surfs.pop(0)
    message_surfs.append(message_to_surface(message))


text_from_socket = b''


def read_from_socket():
    global connection, text_from_socket, running
    try:
        data = connection.recv(2048)
    # 处于非阻塞模式导致的错误
    except BlockingIOError:
        return

    # 当连接关闭时停止程序
    if not data:
        running = False
    for char in data:
        char = bytes([char])
        if char == b'\n':
            # 将来自服务器的消息从字节转换为单个字符串,并绘制出来
            add_message(text_from_socket.strip().decode('utf-8'))
            text_from_socket = b''
        else:
            text_from_socket += char


def redraw_screen():
    screen.fill(bg_color)

    typing_surf = message_to_surface("> " + typing_text)
    y = screen_height - typing_surf.get_height()
    screen.blit(typing_surf, (0, y))

    message_index = len(message_surfs) - 1
    while y > 0 and len(message_index >= 0):
        message_surf = message_surfs[message_index]
        message_index -= 1
        y -= message_surf.get_height() + message_spacing
        screen.blit(message_surf, [0, y])
    pygame.display.flip()


# 在开始时,屏幕上没有文本信息
running = True
typing_text = ""
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if typing_text:
                    # 删除已显示文本消息的最后一个字符
                    typing_text = typing_text[:-1]
            elif event.key == pygame.K_RETURN:
                add_message('You: ' + typing_text)
                connection.send(typing_text.encode('utf-8') + b'\r\n')
                typing_text = ""
            else:
                # 将用户键入的字母加入到已显示的文本消息中
                typing_text += event.unicode
    read_from_socket()
    redraw_screen()
pygame.quit()
connection.close()
