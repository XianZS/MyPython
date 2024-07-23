"""
    当需要大量船舰一个类的实例的时候，可以使用工厂模式。
    即，从原生的使用类的构造去创建对象的形式，迁移到，基于工厂提供的方法去创建对象的形式。
    操作：
        定一个对象py，然后设置一个接口，就可以随意调用
"""
import sys
import os
from FuncClass import make


def main1():
    # 创建接口
    oj = make()
    # 创建一个Stu对象
    stu1 = oj.getClass("Stu")
    stu2 = oj.getClass("Stu")
    # 创建一个Tea对象
    tea1 = oj.getClass("Tea")
    tea2 = oj.getClass("Tea")
    # 创建一个Sch对象
    sch1 = oj.getClass("Sch")
    sch2 = oj.getClass("Sch")
    sch1.name = "kom"
    sch1.num = 42209210710
    print(sch1.name, sch1.num)
    print(id(sch1), id(sch2))


if __name__ == '__main__':
    main1()
