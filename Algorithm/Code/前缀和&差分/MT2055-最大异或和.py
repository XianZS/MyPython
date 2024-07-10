"""
链接：https://www.matiji.net/exam/brushquestion/55/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：前缀异或和
"""
import sys
import os


def main():
    n = int(input())
    als = list(map(int, input().split()))
    nums = [0 for _ in range(n + 1)]
    for x in range(1, n + 1):
        nums[x] = nums[x - 1] ^ als[x - 1]
    # print(nums)
    res = 0
    for x in range(1, n + 1):
        for y in range(n, x - 1, -1):
            res = max(res, nums[y] ^ nums[x - 1])
    print(res)
    return 0


if __name__ == '__main__':
    main()
