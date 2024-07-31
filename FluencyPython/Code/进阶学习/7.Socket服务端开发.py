"""
    Socket(套接字)是进程之间通信的一个工具：
    负责进程之间的网络数据传输，好比数据的搬运工

                        |--->客户端
    -------    回复      |       |
    |服务端|-------------|       |
    -------                     |
        |           发送         |
        <-----------------------|
"""
import sys
import os
import socket


def main():
    # [1]创建socket对象
    socket_server = socket.socket()
    # [2]绑定ip地址和端口号
    # 传入参数为"二元元组"，tuple[0]为IP地址，tuple[1]为端口号
    socket_server.bind(("127.0.0.1", 8888))
    # [3]监听端口
    # 传入参数为int，表示接受的连接数量
    socket_server.listen(1)
    # [4]等待客户端链接
    # 返回值为"二元元组",tuple[0]表示客户端和服务端的连接对象，tuple[1]表示客户端的地址信息
    # .accept()方法为阻塞方法，如果没有客户端连接，则会一直停留在此处
    conn, address = socket_server.accept()
    print(f"conn:{conn},address:{address}")
    while True:
        # [5]接收客户端信息
        # conn.recv(缓冲区大小，一般1024).decode(解码形式)
        # --- return : 字节数组bytes对象，不是字符串对象，可以通过decode()方法将字节数组转换为字符串
        ke_hu_duan = conn.recv(1024).decode("UTF-8")
        print(f"客户端发送的信息为:", ke_hu_duan)
        if ke_hu_duan == "再见":
            break
        # [6]发送回复消息
        msg = input("请输入你回复的消息：").encode("UTF-8")
        conn.send(msg)
    # [7]关闭链接
    conn.close()
    socket_server.close()


if __name__ == '__main__':
    main()
