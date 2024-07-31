"""
    客户端开发
"""
import socket


def main():
    # [1]创建socket对象
    socket_client = socket.socket()
    # [2]连接到服务端
    socket_client.connect(("localhost", 8888))
    # [3]发送数据
    socket_client.send("你好".encode("UTF-8"))
    # [4]接收返回数据
    recv_data = socket_client.recv(1024)
    print(recv_data.decode("UTF-8"))
    # [5]关闭
    socket_client.close()


if __name__ == '__main__':
    main()
