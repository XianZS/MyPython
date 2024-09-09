"""
    通过isinstance(对象,类型)判断该对象是否具备某一个类型
"""
from collections.abc import Sized


class Stu:
    def __init__(self, student_list):
        self.student_list = student_list

    def __getitem__(self, item):
        return self.student_list[item]

    def __len__(self):
        return len(self.student_list)


student = Stu(["aom", "som", "dom"])
print(isinstance(student, Sized))

"""
抽象基类：
    from abc import ABC, abstractmethod
    抽象基类必须继承ABC类
    当子类想要继承父类时，必须重写父类中的方法，如果没有重写，则会报错。
"""
from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get_cache(self):
        pass

    @abstractmethod
    def set_cache(self, value):
        pass


class TulingOnline(Cache):
    def get_cache(self):
        pass

    def set_cache(self, value):
        pass


Online = TulingOnline()
