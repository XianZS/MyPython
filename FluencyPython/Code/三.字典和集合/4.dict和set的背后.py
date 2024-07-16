import os
import sys


def main() -> None:
    """
        dict的规则
        [1] 键必须是可散列的
        [2] 内存开销巨大
            因为字典使用了散列表，而散列表又必须是可稀疏的，这导致它在空间上效率低下
            (如果需要存放大量数据，最好使用元组或者具有元组构成的列表)
        [3] 键查询很快
            dict是典型的时间换空间(字典类型具有巨大的内存开销)，但是它们无视数据量的大小可以进行快速访问
            如假设访问数据量为1000的dict，花费的时间是t，那么访问数据量为10000000的dict，所花费的时间大约是2.8t，每秒大概可以进行200万个键查询
        [4] 键的次序取决于添加顺序
        [5] 往字典中添加新键，可能会改变已有键的顺序
    """
    pass


if __name__ == '__main__':
    main()
