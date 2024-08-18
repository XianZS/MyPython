"""
    类属性(a)绑定类对象A
    实例属性(b/c)绑定实例对象x
    类对象无法访问实例对象，因为只有在实例化对象时，实例属性才会被初始化
"""


class A:
    # 类属性 a
    a = 1

    def __init__(self, b=None, c=None):
        # 实例属性 b和c
        self.b = b
        self.c = c

    def __str__(self):
        return "类属性和实例属性的区别"


# code(1):打印类属性、实例属性
x1 = A(2, 3)
x2 = A(4, 5)
print(x1.a, x1.b, x1.c)  # 1 2 3
print(x2.a, x2.b, x2.c)  # 1 4 5

# code(2):通过“类对象”修改“类属性”，可以成功
A.a = 3
print(A.a)  # 3
print(x1.a)  # 3

# code(3):通过“实例对象”修改类属性，只能修改当前实例的类属性，无法实现真正意义上的全局修改
x1.a = 7
print(A.a)  # 3
print(x1.a)  # 7
