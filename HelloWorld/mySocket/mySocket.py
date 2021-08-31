import socket


# 从套接字服务器上响应用户输入
#########################
# 启动服务器接收1个连接
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind(('::', 12345))
s.listen(1)
connection, from_address = s.accept()
connection.sendall(b"Hi there! Welcome to my server!\r\nWhat's your name? ")
# 每次从客户端读取1字节数据
name = bytes()
while True:
    # 等待客户端发送1字节的数据
    next_character = connection.recv(1)
    # 当按下回车键或没有更多数据时停止读取
    if next_character in [b'', b'\r', b'\n']:
        break
    else:
        name += next_character
connection.sendall(b"Nice to meet you, " + name + b"! Goodbye for now!\r\n")
connection.shutdown(socket.SHUT_WR)
connection.close()
s.close()


# 一台简单的套接字服务器
####################
# # 创建一个套接字供服务器使用
# s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# # 将套接字绑定到端口 12345 上
# s.bind(('::', 12345))
# # 监听连接
# s.listen(1)
# # 等待连接
# connection, from_address = s.accept()
# # 向套接字连接发送一条响应消息
# connection.sendall(b"Hi there--oops, sorry, gotta go!\r\n")
# # 关闭连接
# connection.shutdown(socket.SHUT_WR)
# connection.close()
# # 关闭服务器套接字
# s.close()


# 利用 socket 模块构造 HTTP 请求
#############################
# connection = socket.create_connection(('helloworldbook3.com', 80))
# connection.sendall('GET /data/message.txt HTTP/1.0\r\n'.encode('utf-8'))
# connection.sendall(b'Host: helloworldbook3.com\r\n\r\n')
# # 接收返回的消息
# response = bytes()
# while True:
#     new_data = connection.recv(4096)
#     if not new_data:
#         break
#     response += new_data
# print(response.decode('utf-8'))
# connection.close()

# hello_str = "Hello!"
# hello_bytes = hello_str.encode('utf-8')
# print(list(hello_bytes))
# secret_word = bytes([112, 105, 122, 122, 97])
# print(secret_word.decode('utf-8'))

# some_bytes = b"pepperoni"
