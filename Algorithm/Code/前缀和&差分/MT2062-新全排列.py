"""
链接：https://www.matiji.net/exam/brushquestion/62/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：前缀和
"""
import sys
import os
import collections


def main():
    n = int(input())
    als = list(map(int, input().split()))
    nums = [0 for _ in range(n)]
    for x in range(1, n):
        nums[x] = nums[x - 1] + als[x - 1]
    # print(nums)
    min_num = min(nums)
    add_num = 1 - min_num
    for x in range(n):
        nums[x] += add_num
    dnums = [1 for _ in range(n)]
    for cho in nums:
        try:
            dnums[cho - 1] = 0
        except:
            return 1
    if sum(dnums):
        return 1
    else:
        for cho in nums:
            print("%d " % cho, end='')


if __name__ == '__main__':
    judge = main()
    if judge:
        print(-1)
