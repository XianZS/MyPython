from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "/home/xzs/pyCode/MyPython/venv/bin/python"

os.environ['HADOOP_HOME'] = "/home/xzs/hadoop/"
conf = SparkConf().setMaster("local").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9])
rdd.saveAsTextFile("out", compressionCodecClass=None)
