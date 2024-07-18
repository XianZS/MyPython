from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)


def main():
    rdd = sc.parallelize(["jom hom gom", "kom fom", "lom dom som aom"])
    rdd2 = rdd.map(lambda x: x.split())
    print(rdd2.collect())
    # [['jom', 'hom', 'gom'], ['kom', 'fom'], ['lom', 'dom', 'som', 'aom']]
    # 可以看到，这属于一个二位列表，但是我们想要的是存储着所有单词的一个一维列表
    rdd3 = rdd.flatMap(lambda x: x.split())  # flatMap可以解除嵌套
    print(rdd3.collect())
    # ['jom', 'hom', 'gom', 'kom', 'fom', 'lom', 'dom', 'som', 'aom']


if __name__ == '__main__':
    main()
