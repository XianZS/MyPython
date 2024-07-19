from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"

os.environ['HADOOP_HOME'] = "D:/program/hadoop/hadoop-3.3.4"
conf = SparkConf().setMaster("local").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])
rdd.saveAsTextFile("out", compressionCodecClass=None)
