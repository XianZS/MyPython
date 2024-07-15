from collections import abc


def main() -> int:
    als = [("jom", 88), ("kom", 99), ("lom", 86),
           ("hom", 87), ("gom", 91), ("fom", 66),
           ("dom", 97), ("som", 95), ("aom", 94)]
    # 字典推导式，迭代一次
    stu = {name: number for name, number in als}
    print(stu)
    # 字典推导式，迭代stu字典，并且将学生姓名全部改为大写
    new_stu = {number: name.upper() for name, number in stu.items()}
    print(new_stu)
    return 0


if __name__ == '__main__':
    main()
