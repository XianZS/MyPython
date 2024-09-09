"""
    创建字典子类
"""
print()


class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = MyDict()
my_dict["jom"] = 3
my_dict["kom"] = 4
my_dict["lom"] = 5
print(my_dict)
