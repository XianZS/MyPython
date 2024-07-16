"""
    数据存储方式：RDD对象
"""
from pyspark import SparkConf, SparkContext


def main() -> int:
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    # sc.parallelize()迭代python类型数据
    rdd1 = sc.parallelize([1, 2, 3])
    rdd2 = sc.parallelize((1, 2, 3))
    rdd3 = sc.parallelize({1, 2, 3})
    rdd4 = sc.parallelize("123")
    rdd5 = sc.parallelize({"key1": 1, "key2": 2, "key3": 3})
    print(rdd1)
    print(type(rdd1))
    print(rdd1.collect())
    print(rdd2.collect())
    print(rdd3.collect())
    print(rdd4.collect())
    print(rdd5.collect())
    sc.stop()
    return 0


def main1():
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
    sc = SparkContext(conf=conf)
    rdd = sc.textFile("../note/example.txt")
    print(rdd.collect())
    sc.stop()


if __name__ == '__main__':
    main()
    main1()
