class A:
    pass


class B(A):
    pass


"""
    isinstance(被判断类型，类型)判断传入的对象是不是指定的类型
    并且，被判断对象也会参考继承关系。
"""
b = B()
print(isinstance(b, B))
print(isinstance(b, A))

"""
    == 是判断两个值是否相等
"""
print(type(b) == B)
print(type(b) == A)

"""
    is 判断的是内存地址
"""
print(type(b) is B)
print(type(b) is A)
