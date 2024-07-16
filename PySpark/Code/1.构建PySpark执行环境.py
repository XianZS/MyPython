from pyspark import SparkConf, SparkContext

# 创建SparkConf对象，当前Spark的运行模式和名字
conf = SparkConf().setMaster("local[*]"). \
    setAppName("test_spark_app")
# 基于SparkConf对象，创建SparkContext对象
sc = SparkContext(conf=conf)


# # 打印PySpark运行版本
# print(sc.version, end='')
# # 停止SparkContext对象的运行
# sc.stop()
def main():
    als = [x for x in range(10)]
    print(als)
    sc.parallelize(als)


if __name__ == '__main__':
    main()
