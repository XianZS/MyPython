import sys
import os

"""
    装饰器基础写法
"""


def outer(func):
    def inner():
        print("开始睡觉")
        func()
        print("开始起床")

    return inner


def sleep():
    from random import randint
    import time
    print("睡觉中……")
    time.sleep(randint(1, 10))


# if __name__ == '__main__':
#     fn = outer(sleep)
#     # fn实质上是inner()函数
#     fn()


"""
    装饰器高阶写法
"""


def outer1(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我要起床了")

    return inner


"""
    将装饰器修饰的函数，作为传入参数传入
"""


@outer1
def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint(1, 10))


sleep()
