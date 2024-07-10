"""
链接：https://matiji.net/exam/brushquestion/59/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：前缀和
"""
import sys
import os


def main():
    n = int(input())
    als = list(map(int, input().split()))
    nums = [0 for _ in range(n + 1)]
    for x in range(1, n + 1):
        nums[x] = nums[x - 1] + als[x - 1]
    # print(nums)
    num = sum(als)
    res = 0
    for x in range(2, n+1):
        if nums[x - 1] == num - nums[x - 1]:
            res += 1
    print(res)
    return 0


if __name__ == '__main__':
    main()
