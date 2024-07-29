import threading
import time

"""
    基础使用
"""


# 线程1
def make1():
    while True:
        print("make1")
        time.sleep(1)


# 线程2
def make2():
    while True:
        print("make2")
        time.sleep(1)


def main():
    # 创建线程1
    obj1 = threading.Thread(target=make1)
    # 创建线程2
    obj2 = threading.Thread(target=make2)
    obj1.start()
    obj2.start()


"""
    传入参数:元组|字典
"""


def make3(name):
    for _ in range(5):
        print(name)
        time.sleep(1)


def make4(name):
    for _ in range(5):
        print(name)
        time.sleep(1)


def main1():
    # 创建进程obj3,其含有传入参数,传参形式为元组:args=("jom",)
    obj3 = threading.Thread(target=make3, args=("jom",))
    # 创建进程obj4,其含有传入参数,传参形式为字典:kwargs={"name":"kom"}
    obj4 = threading.Thread(target=make4, kwargs={"name": "kom"})
    obj3.start()
    obj4.start()


if __name__ == '__main__':
    # main()
    main1()
