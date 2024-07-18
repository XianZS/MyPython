from pyspark import SparkConf, SparkContext
import os
from random import randint

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)


def main() -> None:
    """
        distinct算子：去重操作
    """
    nums = [randint(1, 10) for _ in range(20)]
    print(nums)
    # >>> [4, 2, 5, 8, 1, 4, 6, 9, 10, 9, 1, 6, 1, 10, 7, 4, 1, 8, 2, 8]
    rdd = sc.parallelize(nums)
    rdd1 = rdd.distinct()
    print(rdd1.collect())
    # >>> [1, 2, 4, 5, 6, 7, 8, 9, 10]


if __name__ == '__main__':
    main()
