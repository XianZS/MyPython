from pyspark import SparkConf, SparkContext
# 因为spark是运行在分布式集群上面的，所以当在Spark运行时，需要指定当前运行环境的python解释器
import os

os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")

sc = SparkContext(conf=conf)


def add(data):
    return data * 10


def main() -> None:
    nums = [x for x in range(1, 10)]
    rdd = sc.parallelize(nums)
    # (T) -> U: 表示map()方法传入的参数为一个函数，并且这个函数有一个传入参数，有一个返回值
    # lambda 传入参数:处理逻辑
    rdd1 = rdd.map(lambda x: x * 10)
    print(rdd1.collect())
    # >>> [10, 20, 30, 40, 50, 60, 70, 80, 90]


def main1() -> None:
    """
    链式调用
    """
    rdd_pointer = sc.parallelize([x for x in range(1, 11)])
    print(rdd_pointer.collect())
    # >>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rdd_res = rdd_pointer.map(lambda x: x * 10).map(lambda x: x + 2)
    print(rdd_res.collect())
    # [12, 22, 32, 42, 52, 62, 72, 82, 92, 102]


if __name__ == '__main__':
    main()
    main1()
