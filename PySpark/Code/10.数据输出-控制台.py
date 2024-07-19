from pyspark import SparkConf, SparkContext
import os
from random import randint

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([randint(1, 20) for _ in range(10)])

"""
    [1]使用collect算子，输出rdd为list对象
"""
rdd_list: list = rdd.collect()
print(rdd_list, type(rdd_list))
# [6, 7, 17, 17, 13, 3, 17, 11, 14, 11] <class 'list'>

"""
    [2]使用reduce算子
    reduce处理数据时有着一对一的特性，而reduceByKey则有着多对一的特性。比如reduce中会把数据集合中每一个元素都处理一次，并且每一个元素都对应着一个输出。而reduceByKey则不同，它会把所有key相同的值处理并且进行归并，其中归并的方法可以自己定义。
    将rdd中的元素依次传入，对其两两进行操作，返回一个结果
"""
number = rdd.reduce(lambda x, y: x + y)
print(number, type(number))
# 122 <class 'int'>


"""
    [3]take(n)算子
    得到rdd的前n个元素
"""
rdd_take_list = rdd.take(3)
print(rdd_take_list, type(rdd_take_list))
# [9, 2, 15] <class 'list'>

"""
    [4]count算子
    计算rdd内有多少个元素
"""
rdd_len = rdd.count()
print(rdd_len, type(rdd_len))
# 10 <class 'int'>
