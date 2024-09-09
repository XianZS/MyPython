"""
自省机制：
    所谓自省机制，就是检测一个类的内部结构：

print(类.__dict__)
    会输出当前类的自身属性，但是不会检查当前类对象的父类
    return.type=dict

stu实例是Student类对象的实例对象，如果向给stu单独添加某个属性，可以使用如下写法：
    stu.__dict__["address"]="上海"

dir():
    函数可以查询一个对象中的所有属性和方法，包含这个对象的父类
    return.type=list
"""


class Person:
    name = "user"


class Student(Person):
    """
        Student
    """

    def __init__(self, school_name):
        self.school_name = school_name


stu = Student("图灵学院")

# code(1):查询这个对象包含的属性
print(stu.__dict__)
print(Student.__dict__)

# code(2):给某个实例对象临时添加某个属性
stu.__dict__["address"] = "长沙"
print(stu.address)

# code(3):
print(dir(stu))
