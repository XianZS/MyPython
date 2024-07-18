# 常见算子
* map算子
* flatMap算子
* reduceByKey算子
* filter算子
* distinct算子
* sortBy算子
# 1、map算子
## 作用
(T) -> U
<br>
&emsp;&emsp;传入参数为一个函数，并且这个函数有一个任意类型的返回值.
<br>
&emsp;&emsp;它会将rdd中的每个元素拿出来，进行func操作
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd_pointer = sc.parallelize([x for x in range(1, 11)])
print(rdd_pointer.collect())
# >>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd_res = rdd_pointer.map(lambda x: x * 10).map(lambda x: x + 2)
print(rdd_res.collect())
```
# 2、flatMap算子
## 作用
&emsp;&emsp;解除嵌套
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd = sc.parallelize(["jom hom gom", "kom fom", "lom dom som aom"])
rdd1 = rdd.flatMap(lambda x: x.split())  # flatMap可以解除嵌套
print(rdd1.collect())
```
# 3、reduceMap算子
## 作用
&emsp;&emsp;reduceByKey算子主要针对KV型RDD，自动按照key分组，然后根据设定好的聚合逻辑，完成组内数据的聚合操作。
kv型RDD：[(x1,x2),(y1,y2),(z1,z2),(p1,p2)]
key：nums[x][0] for x in range(n)
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)
# 构建KV型RDD对象
nums = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 3), ('c', 1)]
rdd = sc.parallelize(nums)
# 在这里使用reduceByKey算子，分组之后完成组内聚合
res = rdd.reduceByKey(lambda x, y: x + y)
print(res.collect())
```
# 4、filter算子
## 作用
&emsp;&emsp;根据func返回结果进行数据筛选。
&emsp;&emsp;当func返回结果为True时，保留当前枚举的值，反之，则不保留当前的值
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
import random
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)
def judge(number: int) -> bool:
    """
        当前数字大于0，并且当前数字为奇数，返回True，反之返回False
    """
    return number > 0 and number & 1
def main():
    """
        filter算子：如果传入函数的返回值为True，保留当前数据，反之，舍弃当前数据
    """
    als = [random.randint(-50, 50) for x in range(100)]
    rdd = sc.parallelize(als)
    rdd1 = rdd.filter(judge)
    print(rdd1.collect())
    # >>> [43, 43, 25, 5, 43, 33, 41, 31, 45, 43, 35, 23, 15, 15, 33, 11, 31, 9, 39, 21, 23, 27, 41, 25, 11, 31, 49,
    # 3, 11, 7]
```
# 5、distinct算子
## 作用
&emsp;&emsp;对当前rdd中的元素进行去重操作。
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
from random import randint
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
sc = SparkContext(conf=conf)
def main() -> None:
    """
        distinct算子：去重操作
    """
    nums = [randint(1, 10) for _ in range(20)]
    print(nums)
    # >>> [4, 2, 5, 8, 1, 4, 6, 9, 10, 9, 1, 6, 1, 10, 7, 4, 1, 8, 2, 8]
    rdd = sc.parallelize(nums)
    rdd1 = rdd.distinct()
    print(rdd1.collect())
```
# 6、sortBy算子
## 作用
&emsp;&emsp;对根据排序规则func对当前rdd中的元素进行排序
## 示例代码
```python
from pyspark import SparkConf, SparkContext
import os
import random
os.environ['PYSPARK_PYTHON'] = "D:/program/pycharm/code/MyPython/venv/Scripts/python.exe"
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark")
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
```