"""
    在python中，对象是指在内存中具有唯一表识符、类型和值的实例。
    换句话说，它是一个具有属性和方法的实体，这些属性和方法可以被访问和操作。
"""
# code:(1)
num: int = 10
print(id(num))


# 所谓对象其实就是保存在内存中的一段数据

# code:(2)
def add(a, b):
    return a + b


new = add

print(id(new), id(add))


# code:(3)
class Person:
    def __init__(self):
        print("time")


print(id(Person))

# code:(4)
# 将上述的函数对象和类对象添加到容器之中
obj = list()
obj.append(add)
obj.append(Person)
for cho in obj:
    print(cho)


# code:(5)
# 通过装饰器的方式
# 装饰器就是在不改变原函数内部代码的情况下，使用新的函数修饰原函数
def my_wrapper(func_obj):
    # 当前外部函数接收的是一个函数对象
    def wrapper():
        print("这是一个装饰器")
        func_obj()

    # 外部函数返回的是内部函数对象/引用
    return wrapper


# 这里使用@语法糖，将外函数用作于修饰原函数
@my_wrapper
def print_wrapper():
    print("这是一个测试函数")


print_wrapper()
