"""
    闭包
    由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占有内存。
"""
import sys
import os


def main1(num1):
    """
        内部函数使用外部变量。
        作用：这样可以完美实现，既依赖于全局变量，也不想该全局变量被修改。
    """

    def judge(num2: int):
        return num1 == num2

    return judge


def main2(num: int):
    """
        当想要在闭包中修改外部变量，则需要使用 nonlocal 关键字
    """

    def make(num1: int):
        nonlocal num
        num += num1
        print(num)

    return make


def main3(als=0):
    def atm(num: int, make: bool):
        nonlocal als
        if make:
            als += num
            return True
        else:
            if als >= num:
                als -= num
                return True
            print("账户余额不足,", end='')
            return False

    return atm


if __name__ == '__main__':
    xxx1 = main1(3)
    print(xxx1(4), type(xxx1))
    # False <class 'function'>
    xxx2 = main2(3)
    xxx2(4)
    xxx3 = main3()
    if xxx3(7, True):
        print("操作成功")
    else:
        print("操作失败")
    if xxx3(4, False):
        print("操作成功")
    else:
        print("操作失败")
    if xxx3(4, False):
        print("操作成功")
    else:
        print("操作失败")
