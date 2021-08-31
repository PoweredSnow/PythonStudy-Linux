import select
import socket

# 启动服务器并监听连接
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('::', 12345))
server_socket.listen()
# 设置套接字为非阻塞模式
server_socket.setblocking(False)

client_sockets = []
client_objects = {}


class Client:
    def __init__(self, socket):
        self.socket = socket
        self.text_typed = b""
        self.username = None

        socket.setblocking(False)
        msg = b'Welcome to the chat server!\r\n'
        msg += b'Please enter a username:\r\n'
        socket.send(msg)

    def receive_data(self):
        # 每次最多读取 2048 字节
        data = self.socket.recv(2048)
        # 当没有更多数据可以读取时，也就意味着客户端已经关闭了连接
        if not data:
            self.close_connection()
            return
        for char in data:
            char = bytes([char])
            # 当用户按下回车键时，就发送已键入的消息
            if char == b'\n':
                self.handle_command(self.text_typed.strip())
                self.text_typed = b""
            else:
                self.text_typed += char

    def handle_command(self, command):
        global client_objects
        if self.username == None:
            self.username = command
            msg = b'Hi, ' + self.username + b'!'
            msg += b' Type a message and press Enter to send it.\r\n'
            self.socket.send(msg)
        elif command == b'/quit':
            self.close_connection()
        else:
            msg = b'[' + self.username + b']: ' + command + b'\r\n'
            # 将消息发送给服务器上的其他所有用户
            for client_object in client_objects.values():
                if client_object == self or client_object.username == None:
                    continue
                client_object.socket.send(msg)

    def close_connection(self):
        global client_sockets, client_objects
        client_sockets.remove(self.socket)
        del client_objects[self.socket.fileno()]
        self.socket.close()


while True:
    # 等待其中任意套接字上收到消息
    ready_to_read = select.select([server_socket] + client_sockets, [], [])[0]
    for sock in ready_to_read:
        # 服务器获得新连接
        if sock == server_socket:
            new_connection, address = sock.accept()
            client_sockets.append(new_connection)
            client_objects[new_connection.fileno()] = Client(new_connection)
            server_socket.listen()
        # 某个现有客户端发送数据或关闭连接
        else:
            client_objects[sock.fileno()].receive_data()
