# from pyspark import SparkConf, SparkContext
# import os
#
# os.environ['PYSPARK_PYTHON'] = "/home/xzs/pyCode/MyPython/venv/bin/python"
#
# os.environ['HADOOP_HOME'] = "/home/xzs/hadoop/"
# conf = SparkConf().setMaster("local").setAppName("test_spark")
# 设置全局变量
# conf.set("spark.default.parallelism", "1")
# sc = SparkContext(conf=conf)
#
#
# def main() -> None:
#     rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])
#     rdd.saveAsTextFile("OutList", compressionCodecClass=None)
#
#
# def main1() -> None:
#     rdd = sc.parallelize((1, 2, 3, 4, 5, 6, 7, 8, 9))
#     rdd.saveAsTextFile("OutTuple", compressionCodecClass=None)
#
#
# def main2() -> None:
#     rdd = sc.parallelize({1, 2, 3, 4, 5, 6, 7, 8, 9})
#     rdd.saveAsTextFile("OutSet", compressionCodecClass=None)
#
#
# def main3() -> None:
#     rdd = sc.parallelize({1: 2, 3: 4, 5: 6, 7: 8})
#     rdd.saveAsTextFile("OutDict", compressionCodecClass=None)
#
#
# def main4() -> None:
#     rdd = sc.parallelize("123456789")
#     rdd.saveAsTextFile("OutStr", compressionCodecClass=None)
#
#
# if __name__ == '__main__':
#     main()
#     main1()
#     main2()
#     main3()
#     main4()

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "/home/xzs/pyCode/MyPython/venv/bin/python"

os.environ['HADOOP_HOME'] = "/home/xzs/hadoop/"
conf = SparkConf().setMaster("local").setAppName("test_spark")
sc = SparkContext(conf=conf)


def main() -> None:
    # 设置局部变量
    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
    rdd.saveAsTextFile("OutList", compressionCodecClass=None)


def main1() -> None:
    # 设置局部变量
    rdd = sc.parallelize((1, 2, 3, 4, 5, 6, 7, 8, 9), 1)
    rdd.saveAsTextFile("OutTuple", compressionCodecClass=None)


def main2() -> None:
    rdd = sc.parallelize({1, 2, 3, 4, 5, 6, 7, 8, 9}, 1)
    rdd.saveAsTextFile("OutSet", compressionCodecClass=None)


def main3() -> None:
    rdd = sc.parallelize({1: 2, 3: 4, 5: 6, 7: 8}, 1)
    rdd.saveAsTextFile("OutDict", compressionCodecClass=None)


def main4() -> None:
    rdd = sc.parallelize("123456789", 1)
    rdd.saveAsTextFile("OutStr", compressionCodecClass=None)


if __name__ == '__main__':
    main()
    main1()
    main2()
    main3()
    main4()
