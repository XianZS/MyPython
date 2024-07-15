"""
[main]
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=10)
deque([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], maxlen=10)
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=10)
deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], maxlen=10)
deque([0, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=10)
deque([5, 6, 7, 8, 9, 10, 11, 12, 13, 14], maxlen=10)
deque([3, 2, 1, 0, 5, 6, 7, 8, 9, 10], maxlen=10)
"""

import sys
import os
from collections import deque


def main() -> None:
    dq = deque(range(1, 11), maxlen=10)
    # 输出一下dq数组
    print(dq)
    # 将dq数组尾部n个数字移到头部，右边--->左边
    dq.rotate(3)
    print(dq)
    # 将dq数组头部n个数字移到尾部，左边--->右边
    dq.rotate(-3)
    print(dq)
    # 对dq数组尾部添加元素，它dq数组头部的元素会被挤出
    dq.append(11)
    print(dq)
    # 对dq数组头部添加元素，它dq数组尾部的元素会被挤出
    dq.appendleft(0)
    print(dq)
    # 对dq数组追加列表也是一样的，给尾部添加列表，头部元素会被依次挤出
    dq.extend(range(11, 15))
    print(dq)
    # 但是，当对dq数组头部进行添加列表时nums，尾部元素会被依次挤出，这里需要注意的是，nums的第一个元素最先被添加，然后其余元素按照下标，从小到大依次被加入头部
    dq.extendleft(range(0, 4))
    print(dq)


if __name__ == '__main__':
    main()
