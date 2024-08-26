data_list = [x for x in range(1, 21)]
# 切片的常规操作
# print(data_list[::])
# print(data_list[::-1])
# print(data_list[::2])
# print(data_list[:10], end='')

"""
    自定义支持切片的序列类
"""

from collections import abc


class PersonGroup:
    def __init__(self, group_name, school_name, staffs: list):
        self.group_name = group_name
        self.school_name = school_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    # 实现切片的关键方法
    def __getitem__(self, item):
        return self.staffs[item]

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass


stu_group = PersonGroup("python小组", "图灵学院", ["fom", "gom", "hom", "jom", "kom", "lom"])
print(stu_group[::-1])
print(stu_group.__reversed__())
