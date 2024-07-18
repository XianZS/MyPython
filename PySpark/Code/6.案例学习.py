from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
# 构建执行环境入口对象
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)


def main() -> None:
    # 读取文件
    rdd = sc.textFile("../note/example1.txt")
    print(rdd.collect())
    rdd1 = rdd.flatMap(lambda x: x.split()) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y)
    print(rdd1.collect())
    # >>> [('python', 2), ('java', 2), ('Good', 1), ('C', 2), ('RUST', 1), ('R', 1), ('Master', 1), ('Run', 1),
    # ('first', 1), ('second', 1)]


if __name__ == '__main__':
    main()
