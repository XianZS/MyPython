"""
链接：https://www.matiji.net/exam/brushquestion/53/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：[1]滚动窗口 [2]前缀和
"""
import sys
import math


def main():
    n, k, b = map(int, input().split())
    b = min(b, 50000)
    nums = [0 for _ in range(n + 1)]
    for _ in range(b):
        nums[int(input())] = 1
    als = [0 for _ in range(n + 1)]
    for x in range(1, n + 1):
        als[x] = als[x - 1] + nums[x]
    # print(als)
    res = math.inf
    for x in range(k, n + 1):
        res = min(res, als[x] - als[x - k])
    print(res)


if __name__ == '__main__':
    main()
