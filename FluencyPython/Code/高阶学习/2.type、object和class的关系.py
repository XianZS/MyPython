a = 1
b = 'abc'
# code:(1)
# type
print(type(a))
# <class 'int'>

# code:(2)
"""
Python中的数据类型是由类型类创建出来的
Python中的类型是由type创建出来的
"""
print(type(b))
print(type(str))


# <class 'str'>
# <class 'type'>

# code:(3)
class Stu:
    pass


stu = Stu()
print(type(stu))
print(type(Stu))


# <class '__main__.Stu'>
# <class 'type'>


# code:(4)
class a:
    name = None


print(a.__bases__)
# (<class 'object'>,)

# code:(5)
"""
1.object是被type创建的
2.type继承了object
"""
print(type(object))
print(type.__bases__)
# <class 'type'>
# (<class 'object'>,)

# code:(6)
print(object.__bases__)
# ()

# code:(7)
"""
type是由自身创建的
"""
print(type(type))
# <class 'type'>
