"""
总结：
    1.魔术方法可以添加原本类不具有的特性
    2.魔术方法是python解释器提供的，不能随意更改魔术方法的方法名
"""


class Student(object):
    def __init__(self, names):
        self.names = names

    # 魔术方法，让学生类(的某一个属性)具有序列特性
    """
        当不使用该方法时，学生类支持for循环迭代
    """

    def __getitem__(self, item):
        return self.names[item]


student1 = Student(["jom", "kom", "lom"])

# for循环必须获取一个迭代器，才能进行数据的迭代
for stu in student1:
    print(stu)
