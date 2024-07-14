"""
链接：https://www.matiji.net/exam/brushquestion/109/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：排序
"""
import sys
import os


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    x1 = []
    x2 = []
    dnums = [0 for _ in range(n)]
    for x in range(n):
        if nums[x] & 1:
            dnums[x] = 1
            x1.append(nums[x])
        else:
            x2.append(nums[x])
    x1.sort()
    x2.sort()
    xx1 = 0
    xx2 = 0
    # print(x1, x2)
    for x in range(n):
        if dnums[x]:
            print(x1[xx1], "", end='')
            xx1 += 1
        else:
            print(x2[xx2], "", end='')
            xx2 += 1


if __name__ == '__main__':
    main()
