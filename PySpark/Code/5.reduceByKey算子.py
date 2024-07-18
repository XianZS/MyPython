from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)


def main():
    """
      reduceByKey算子主要针对KV型RDD，自动按照key分组，
    然后根据设定好的聚合逻辑，完成组内数据的聚合操作。
    kv型RDD：[(x1,x2),(y1,y2),(z1,z2),(p1,p2)]
    key：nums[x][0]
    """
    # 构建KV型RDD对象
    nums = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 3), ('c', 1)]
    rdd = sc.parallelize(nums)
    # 在这里使用reduceByKey算子，分组之后完成组内聚合
    res = rdd.reduceByKey(lambda x, y: x + y)
    print(res.collect())
    # >>> [('b', 4), ('c', 1), ('a', 6)]


if __name__ == '__main__':
    main()
