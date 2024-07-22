from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "/home/xzs/pyCode/MyPython/venv/bin/python"

os.environ['HADOOP_HOME'] = "/home/xzs/hadoop/"

conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("spark_test")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)


def main():
    file_rdd = sc.textFile("./notes.txt", 1)
    ans = file_rdd.map(lambda x: x.split("\t")) \
        .map(lambda x: eval(x[0])) \
        .reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[1], ascending=False)
    """
        [['(1,3)', '21', '博客'], ['(3,2)', '44', '微博'], ['(4,4)', '78', '微信'], ['(5,1)', '90', 'QQ'], ['(6,3)', '97', 'QQ'], ['(3,1)', '88', 'momo'], ['(4,21)', '32', 'ii'], ['(3,0)', '99', 'oo'], ['(1,7)', '89', 'pp']]
        [(1, 3), (3, 2), (4, 4), (5, 1), (6, 3), (3, 1), (4, 21), (3, 0), (1, 7)]
        [(1, 10), (3, 3), (4, 25), (5, 1), (6, 3)]
        [(4, 25), (1, 10), (3, 3), (6, 3), (5, 1)]
    """
    print(ans.collect())


def main1():
    from collections import Counter
    file_rdd = sc.textFile("./notes.txt", 1)
    ans = file_rdd.map(lambda x: x.split("\t")[2])
    res = Counter(ans.collect())
    """
        ['博客', '微博', '微信', 'QQ', 'QQ', 'momo', 'ii', 'oo', 'pp']
        
    """
    print(res.most_common(1)[0][0])
    """
        QQ
    """


def change2(x):
    x[0], x[2] = x[2], eval(x[0])
    return x


def main2():
    file_rdd = sc.textFile("./notes.txt", 1)
    ans = file_rdd.map(lambda x: x.split("\t")) \
        .filter(lambda x: x[2] == "QQ") \
        .map(change2)
    print(ans.collect())
    return ans
    # [['QQ', '90', (5, 1)], ['QQ', '97', (6, 3)]]


def main3():
    file_rdd = sc.textFile("notes.txt")
    ans = file_rdd.map(lambda x: x.split("\t")) \
        .map(lambda x: {"time": eval(x[0]), "number": x[1], "name": x[2]})
    print(ans.collect())
    ans.saveAsTextFile("JSON")
    # [{'time': (1, 3), 'number': '21', 'name': '博客'}, {'time': (3, 2), 'number': '44', 'name': '微博'},
    # {'time': (4, 4), 'number': '78', 'name': '微信'}, {'time': (5, 1), 'number': '90', 'name': 'QQ'},
    # {'time': (6, 3), 'number': '97', 'name': 'QQ'}, {'time': (3, 1), 'number': '88', 'name': 'momo'},
    # {'time': (4, 21), 'number': '32', 'name': 'ii'}, {'time': (3, 0), 'number': '99', 'name': 'oo'},
    # {'time': (1, 7), 'number': '89', 'name': 'pp'}]


if __name__ == '__main__':
    main()
    main1()
    main2()
    main3()
