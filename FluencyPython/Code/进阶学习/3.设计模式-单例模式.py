"""
    单例模式就是对一个类，只获取其唯一的类实例对象，持续复用它
    * 节省内存
    * 节省创建对象的开销
"""
import sys
import os
from Three import thr


def main():
    thr1 = thr
    thr2 = thr
    print(f"{thr1}\t{id(thr1)}")
    print(f"{thr2}\t{id(thr2)}")
    """
        <Three.three object at 0x7f7ce5c376a0>	140174407464608
        <Three.three object at 0x7f7ce5c376a0>	140174407464608
    """


if __name__ == '__main__':
    main()
