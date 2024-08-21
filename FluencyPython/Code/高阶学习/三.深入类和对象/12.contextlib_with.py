import contextlib

"""
    @contextlib.contextmanager通过该装饰器装饰的函数，会支持上限文管理器
    其所装饰的函数，必须是一个生成器对象
"""


@contextlib.contextmanager
def open_file(file_name):
    """
        生成器对象，生成器函数
    """
    print(f"open:{file_name}")
    yield {"name": "jom", "age": 19}
    print(f"close:{file_name}")


with open_file("with测试文件.txt") as f_open:
    print("程序启动")
    print(f_open)