"""
鸭子类型：
    在多个类中实现同一个方法，那么这些类可以看成同一个类。
    (不同的物品，都同时具有某一个相同的属性)
"""


class Cat:
    def say(self):
        print("我是猫")


class Dog:
    def say(self):
        print("我是狗")


class Duck:
    def say(self):
        print("我是鸭子")


animals = [Cat, Dog, Duck]
for cho in animals:
    cho().say()

"""
    可迭代对象
"""


class People:
    def __init__(self, names):
        self.names = names

    def __getitem__(self, item):
        return self.names[item]

    def __len__(self):
        return len(self.names)


now = People(["jom", "kom", "lom"])
aps = ["hom", ]
aps.extend(now)
print(aps)

"""
多态：
    在多个类中同时继承了一个类，并且对父类中的方法进行写
    在每个类中所调用的同一个方法会返回不同的行为
"""


class Animal:
    def run(self):
        print("动物在跑")


class Cat:
    def run(self):
        print("猫在跑")


class Dog:
    def run(self):
        print("狗在跑")


dog = Dog()
cat = Cat()

