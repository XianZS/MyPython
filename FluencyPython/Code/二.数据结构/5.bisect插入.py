import bisect
import random
import time

"""
    bisect.insort(可迭代对象，插入元素)的性能优于普通插入元素之后再排序的性能。
"""


def main():
    index_num = bisect.bisect_right([3, 2, 5, 5, 5, 1, 6], 5)
    print(index_num)
    return True


def main1():
    """
    因为排序很耗时，所以我们有必要在某些时刻，保持序列的有序性
    bisect.insort(可迭代对象,元素)
    """
    nums = []
    begin2 = time.time()
    for _ in range(10):
        nums.append(random.randint(10, 50))
        nums = sorted(nums)
        # print(nums)
    end2 = time.time()
    print(end2 - begin2)
    return True


def main2():
    nums = []
    begin1 = time.time()
    for _ in range(10):
        bisect.insort(nums, random.randint(10, 50))
        # print(nums)
    end1 = time.time()
    print(end1 - begin1)
    return True


if __name__ == '__main__':
    # main()
    # main1()
    # 1.3113021850585938e-05
    # main2()
    # 9.059906005859375e-06
    main()
