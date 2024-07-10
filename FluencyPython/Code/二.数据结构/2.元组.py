import collections


def main():
    als = [("jom", 32), ("kom", 52), ("lom", 42)]
    for name, number in als:
        print(name, " : ", number)


def main1():
    nums = ["jom", "kom", "lom"]
    name1, name2, name3 = nums
    print(name1, name2, name3)


def main2():
    """
    divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
    :return: True
    """
    number = divmod(6, 9)
    """
    res:(0, 6)
    """
    print(number)
    new = (6, 9)
    print(divmod(*new))
    return True


def main3():
    some = ("xxx", "jom", "lom")
    # 在这里，我们对some[0]="xxx"并不感兴趣，所以可以使 _ 来占位
    _, y, z = some
    print(y, z)
    return True


def end():
    print("===<>===")
    return True


if __name__ == '__main__':
    main()
    end()
    main1()
    end()
    main2()
    end()
    main3()
    end()
