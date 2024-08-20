# try-except代码块
# try:
#     print("程序运行")
#     raise KeyError
# except KeyError:
#     print("key error")
# else:
#     print("程序无异常时，运行该语句")
# finally:
#     print("程序无论是否出现异常，都执行此语句")


# 在函数中使用try
def func_try_except_NoError():
    try:
        print("程序运行")
        # raise KeyError
        return 1
    except KeyError:
        print("key error")
        return 2
    else:
        print("程序无异常时，运行该语句")
        return 3
    finally:
        print("程序无论是否出现异常，都执行此语句")
        # 如果finally中出现return，则优先返回finally中的返回值
        # return 4


def func_try_except_Error():
    try:
        print("程序运行")
        raise KeyError
        return 1
    except KeyError:
        print("key error")
        return 2
    else:
        print("程序无异常时，运行该语句")
        return 3
    finally:
        print("程序无论是否出现异常，都执行此语句")
        # 如果finally中出现return，则优先返回finally中的返回值
        # return 4


def func_try_except_IsNotError():
    try:
        print("程序运行")
        # 如果抛出的异常不是捕获语句中的指定异常，则无法正常捕获
        raise FileNotFoundError
        return 1
    except KeyError:
        print("key error")
        return 2
    else:
        print("程序无异常时，运行该语句")
        return 3
    finally:
        print("程序无论是否出现异常，都执行此语句")
        # 如果finally中出现return，则优先返回finally中的返回值
        # return 4


"""
    num1 = func_try_except_NoError()
    print(num1)
    # return_num:1
    num2 = func_try_except_Error()
    print(num2)
    # return_num:2
    num3 = func_try_except_IsNotError()
    print(num3)
    # return_num:报错
"""

"""
    上下文管理协议：with
"""


class Sample:
    def __enter__(self):
        print("我被执行了，__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("我被执行了，__exit__")

    def run(self):
        print("程序启动")


with Sample() as sample:
    sample.run()
    # 当with启动时，自动执行__enter__，输出“我被执行了，__enter__”
    # 程序启动
    # 当with结束时，自动执行__exit__，输出“我被执行了，__exit__”

"""
    文件打开
"""


class OpenFile:
    def __enter__(self):
        try:
            self.file_obj = open("./with测试文件.txt","w")
        except FileNotFoundError:
            self.file_obj = None
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        if self.file_obj is None:
            print("当前文件不存在")
        else:
            # 当前文件存在，关闭该文件
            self.file_obj.close()

    def run(self):
        print("查看文件")

    def Write(self):
        self.file_obj.write("CCC")


with OpenFile() as MyFile:
    MyFile.Write()
