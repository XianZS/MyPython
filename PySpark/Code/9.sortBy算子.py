from pyspark import SparkConf, SparkContext
import os
import random

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_app_spark")
sc = SparkContext(conf=conf)


def main() -> None:
    """
        sortBy()算子：排序
        rdd.sortBy(func,ascending,numPartitions=1)
        - func:(T) -> U：设置排序规则
        - ascending True：升序排序，False：降序排序
        - numPartitions：分区，使用多少区进行排序
    """
    nums = [(random.randint(1, 4), random.randint(1, 11)) for x in range(10)]
    print(nums)
    rdd = sc.parallelize(nums)
    rdd1 = rdd.reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[1], ascending=True, numPartitions=1)
    print(rdd1.collect())
    # [(2, 10), (3, 23), (1, 29)]


if __name__ == '__main__':
    main()
