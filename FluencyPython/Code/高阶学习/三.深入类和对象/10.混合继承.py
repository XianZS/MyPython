"""
混合继承：
    简述：
        当前的继承方式是一种混合继承
    概述：
        1.下面定义了Animal, RunMixin, SwimMixin, FlyMixin四个类，并且每个类之间无固定的继承关系
        2.RunMixin(), SwimMixin(), FlyMixin()这三个类对象中的__init__都调用的name属性，该三个类对象不含有name属性
        3.创建Duck()，类对象让Duck()类对象继承Animal, RunMixin, SwimMixin, FlyMixin
        4.实例化对象duck=Duck()
        5.输出测试，发现即便Animal, RunMixin, SwimMixin, FlyMixin没有固定的继承关系，duck实例对象也能成功输出
    特征：
        1.Mixin的功能是单一的，并没有复杂的继承关系
        2.Mixin类不需要继承其它类(除了object)

"""


class Animal:
    def __init__(self, name):
        self.name = name


class RunMixin:
    def run(self):
        print(f"{self.name}正在跑……")


class SwimMixin:
    def swim(self):
        print(f"{self.name}正在游泳……")


class FlyMixin:
    def fly(self):
        print(f"{self.name}正在飞……")


class Duck(Animal, RunMixin, SwimMixin, FlyMixin):
    pass


duck = Duck("鸭子")
duck.run()
duck.swim()
duck.fly()
