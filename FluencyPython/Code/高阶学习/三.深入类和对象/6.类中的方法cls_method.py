"""
    辨别使用：
        如果当前需求不需要创建实例对象，并且不需要访问实例属性/类属性的情况可以使用静态方法
        如果当前需求不需要创建实例对象，并且需要访问实例属性/类属性的情况可以使用类方法
        如果当前需求需要创建实例对象，并且需要访问实例属性/类属性的情况可以使用实例方法
    * 类方法通常用于操作类级别的属性或执行与类相关的操作。
    * 类实例方法常用于操作实例特定的属性或执行与实例相关的操作。
    * 静态方法适用于在类中组织功能性代码，它们与类和实例无关，但又属于类的逻辑范畴。
"""


class Student:
    address = "China"

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name},{self.age},{self.gender}"

    """
        code(1)
        实例方法
            * 实例方法可以访问类中的属性和方法
            * 可以通过实例对象访问
    """

    def __add_age(self):
        self.age += 1

    def set_age(self):
        self.__add_age()

    """
        code(2)
        静态方法：
            * 静态方法(不能)无法访问类中的属性和方法
        场景：
            在文件中保存了一些学生信息，需要将文件中的信息导入到类中进行处理
        缺点：
            不能访问类属性
            当静态方法返回的是类对象时，当类对象被修改，那么静态方法的返回值也需要被修改
    """

    @staticmethod
    def parse_from_string_1(stu_info):
        name, age, gender = tuple(stu_info.split(','))
        return Student(name, age, gender)

    """
        code(3)
        类方法
            * 类方法可以访问类中的属性和方法
        优点：
            弥补了静态方法的不足之处，传入参数为“def func(cls):”
            可以通过“cls.类属性”访问类属性
    """

    @classmethod
    def parse_from_string_2(cls, stu_info):
        name, age, gender = tuple(stu_info.split(','))
        print(cls.address)
        return cls(name, age, gender)


# code(1):实例方法
stu1 = Student("jom", 28, "男")
print(stu1)
stu1.set_age()
print(stu1)

# code(2):静态方法
# 类对象访问静态方法
stu2 = Student.parse_from_string_1("kom,30,女")
print(stu2)

# code(3):类方法
stu3 = Student.parse_from_string_2("lom,21,男")
print(stu3)
