"""
链接：https://www.matiji.net/exam/brushquestion/90/3181/1DC60EA6DF83A333301CFFE1407FBA59
"""
import sys
import os


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    res = [1 for _ in range(n)]
    for x in range(1, n):
        if nums[x] > nums[x - 1]:
            res[x] = res[x - 1] + 1
        if nums[x] == nums[x - 1]:
            res[x] = res[x - 1]
    for x in range(n - 2, -1, -1):
        if nums[x] > nums[x + 1]:
            res[x] = max(res[x], res[x + 1] + 1)
    print(sum(res))


if __name__ == '__main__':
    main()
