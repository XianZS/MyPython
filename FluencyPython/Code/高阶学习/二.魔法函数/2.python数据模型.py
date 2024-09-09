"""
数据模型:
    其本质就是一个“魔术方法”
    会让原本的类具备某些特性
    如：
        迭代特性: __getitem__
        长度特性：__len__
        自定义详细信息特性：__str__
"""


class Stu:
    def __init__(self, name):
        self.names = name

    def __getitem__(self, item):
        return self.names[item]

    def __len__(self):
        return len(self.names)

    def __str__(self):
        return "这是一个学生类"


stu1 = Stu(["jom", "kom", "lom"])

