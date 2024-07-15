import collections

"""
    集合本质上是许多唯一对象的聚集
"""


def main():
    als = ["jom", "kom", "lom", "kom"]
    als_set = set(als)
    print(als_set)
    name = ["fom", "gom", "kom", "lom"]
    name_set = set(name)
    print(name_set)
    """
    集合运算：[|]合集运算 [&]交集运算 [-]差集运算
    """
    print("[|]合集运算: ", name_set | als_set)
    print("[&]交集运算: ", name_set & als_set)
    print("[-]差集运算: ", name_set - als_set)
    # 比如说，求als_set中元素在name_set中出现的次数
    print("Count: ", len(name_set & als_set))


from dis import dis


def main1():
    """
        集合字面量
        构建方法1：{1, 2, 3}
        构建方法2：set([1, 2, 3])
        构建集合时，构建方法1的速度比构建方法2的速度快
        因为在使用构建方法1时，Python会利用一个叫做BUILD_SET的字节码来创建集合
    """
    print(dis("{1}"))
    print(dis("set([1])"))
    """
    1           0 LOAD_CONST               0 (1)
                2 BUILD_SET                1
                4 RETURN_VALUE
    None
    1           0 LOAD_NAME                0 (set)
                2 LOAD_CONST               0 (1)
                4 BUILD_LIST               1
                6 CALL_FUNCTION            1
                8 RETURN_VALUE
    None
    """
    # 可以看到，dis("{1}")的"BUILD_SET"一条命令，实现了dis("set([1])")的"LOAD_CONST、BUILD_LIST、CALL_FUNCTION"三条命令，所以前者速度更优


def main2():
    """
        集合推导式
    """
    als = [1, 2, 3, 4, 5, 1]
    some = {x for x in als}
    print(some)


def main3():
    """
        集合的操作
    """
    als = {"gom", "hom", "jom", "kom", "lom"}
    # 添加元素
    als.add("nom")
    print(als)
    # 浅复制
    Copy = als.copy()
    print(Copy)
    # 如果集合中存在"kom"，则删去"kom"
    als.discard("kom")
    print(als)
    # 清空集合
    als.clear()
    print(als)


if __name__ == '__main__':
    main()
    main1()
    main2()
    main3()
