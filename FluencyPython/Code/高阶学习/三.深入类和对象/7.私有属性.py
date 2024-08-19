"""
    私有属性无法在一个类的外部使用，只能在类的层面被调用
    在一定程度上保护了某些敏感属性的安全性
    * 如何在类的外部，通过类的实例对象调用私有属性：
        _clsname__私有属性
        如：
            print(p._Person__money)
            可以成功输出Person的私有属性money
"""


class Person:
    def __init__(self, name: str, money: int):
        self.name = name
        # 私有属性money
        self.__money = money

    # 在类的内部访问私有属性
    def get_money(self):
        print(self.__money)


p = Person("jom", 21)
p.get_money()
print(p._Person__money)
