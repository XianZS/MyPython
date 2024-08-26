"""
    bisect可以使用二分查找的方式完成序列的排序的二分插入
"""
import bisect

print()
int_list = list()

# code(1):不断插入新元素，在这个过程中，始终保持原序列的排序规则，默认升序排列
bisect.insort(int_list, 4)
print(int_list)
bisect.insort(int_list, 1)
print(int_list)
bisect.insort(int_list, 3)
print(int_list)
bisect.insort(int_list, 5)
print(int_list)
bisect.insort(int_list, 2)
print(int_list)

# code(2):查找新元素插入的下标
print(bisect.bisect(int_list, 6))
print(int_list)
