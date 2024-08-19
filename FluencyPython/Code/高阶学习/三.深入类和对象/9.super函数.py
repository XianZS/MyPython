"""
    1.super函数的作用
        调用'父类'的方法
        super().'父类'的方法
    2.什么场景下使用super函数
        代码重用的场景下
    3.super函数的运行过程
        super()调用的“类.__mro__”的顺序，并不是调用一个类的父类，而是根据一个类的"__mro__"顺序进行查询并调用
"""


# code(1):super()函数的作用
class a:
    def __init__(self):
        print("A")


class b(a):
    def __init__(self):
        print("B")
        super().__init__()


# code(2):super()函数的应用场景
import threading


class MyThread(threading.Thread):
    def __init__(self, thread_name, user):
        # 重用线程类中定义的属性
        self.user = user
        super().__init__(name=thread_name)


# code(3):
class D:
    def __init__(self):
        print("D")


class C(D):
    def __init__(self):
        print("C")
        super().__init__()


class B(D):
    def __init__(self):
        print("B")
        super().__init__()


class A(B, C):
    def __init__(self):
        print("A")
        super().__init__()


a = A()
print(A.__mro__)
