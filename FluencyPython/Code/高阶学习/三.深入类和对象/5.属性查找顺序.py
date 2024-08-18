"""
    属性：
        * 类属性
        * 实例属性
    向上寻找
    当通过实例对象访问某一个属性时，首先会寻找实例属性(构造方法之中的属性)，然后再寻找类属性
"""

# code(1):
# class A:
#     name = "cla_a"
#
#     def __init__(self):
#         self.name = 'obj_a'
#
#
# x = A()
# # 打印实例属性
# print(x.name, end='')

"""
    菱形继承
"""


class A:
    name = "cls_A"


class B(A):
    name = "cls_B"


class C(A):
    name = "cls_C"


class D(B, C):
    pass


x = D()  # cls_B

# class D(C, B):
#     pass
# x = D() --->cls_C
print(x.name)  # cls_B
# 输出默认查找的类
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

"""
    树状继承
"""


class e:
    name = "cls_e"


class d:
    name = "cls_d"


class c(e):
    name = "cls_c"


class b(d):
    name = "cls_b"


class a(b, c):
    pass


x1 = a()
print(x1.name)  # cls_b
print(a.__mro__)
# (<class '__main__.a'>, <class '__main__.b'>, <class '__main__.d'>, <class '__main__.c'>, <class '__main__.e'>, <class 'object'>)
