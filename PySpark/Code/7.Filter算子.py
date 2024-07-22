from pyspark import SparkConf, SparkContext
import os
import random

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_app_spark")
sc = SparkContext(conf=conf)


def judge(number: int) -> bool:
    """
        当前数字大于0，并且当前数字为奇数，返回True，反之返回False
    """
    return number > 0 and number & 1


def main():
    """
        filter算子：如果传入函数的返回值为True，保留当前数据，反之，舍弃当前数据
    """
    als = [random.randint(-50, 50) for x in range(100)]
    rdd = sc.parallelize(als)
    rdd1 = rdd.filter(judge)
    print(rdd1.collect())
    # >>> [43, 43, 25, 5, 43, 33, 41, 31, 45, 43, 35, 23, 15, 15, 33, 11, 31, 9, 39, 21, 23, 27, 41, 25, 11, 31, 49,
    # 3, 11, 7]


if __name__ == '__main__':
    main()
