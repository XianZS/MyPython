"""
魔术方法：
    （1）数学运算
    （2）非数学运算
"""


class Stu:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def __str__(self):
        return "非测试输出"

    def __repr__(self):
        return "测试输出"


stu = Stu("jom", 89, 10086)
print(stu)
