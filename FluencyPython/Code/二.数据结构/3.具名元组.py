"""
具名元组：
相当于一个只有成员变量的类，但是没有成员方法
class Code:
    def __init__(self,child1,child2):
        self.child1 = child1
        self.child2 = child2
"""
import collections


def main():
    """
        使用namedtuple构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存储在对应的类之中
    这个实例跟普通的对象实例比起来也要小一点，因为python不会用__dict__来从存放这些实例的属性。
    :return: Nonlambdae
    """
    Stu = collections.namedtuple("Stu", ["id", "name", "number"])
    stu1 = Stu(1, "jom", 44)
    stu2 = Stu(2, "kom", 56)
    stu3 = Stu(3, "lom", 44)
    als = []
    als.extend([stu1, stu2, stu3])
    print(als)
    new = sorted(als, key=lambda x: x.number)
    print(new)
    return True


if __name__ == '__main__':
    main()
