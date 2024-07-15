import collections


def main() -> int:
    res = collections.defaultdict(int)
    # 当key不存在时，就会默认创建一个数据/数据类型
    """
    int -> 0
    list -> []
    tuple -> ()
    str -> ""
    set -> {}
    dict -> {}
    """
    print(res[3])
    return 0


def main2():
    """
    虽然Python字典是无序的，但是在Python3.6及之后的版本中，字典变得更加智能。
    其使用了一种称为“保留插入顺序”的技术来存储键值对。
    这种技术确保在字典中添加新键时，它们被添加到最后，并且在迭代字典时按照它们在字典中添加的顺序返回。
    这也就意味着，在Python3.6及之后的版本中，字典的迭代顺序是可以预测的。
    """
    # collections.OrderedDict() 创建一个有序字典
    res = collections.OrderedDict()
    stu = [("jom", 95), ("kom", 87), ("lom", 96)]
    for key, value in stu:
        res[key] = value


def main3():
    als = "dasgufgiuucnnwoi"
    res = collections.Counter(als)
    print(res)
    # 在Counter中封装了"most_common()"方法，用来返回映射关系内最常见的n个键和它们的计数
    ans = res.most_common(1)
    print(ans)
    # 但总而言之，Counter就是把标准dict使用CPython又实现了一边
    return 0


if __name__ == '__main__':
    main()
    main2()
    main3()
