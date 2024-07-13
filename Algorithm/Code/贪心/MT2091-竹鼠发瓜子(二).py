"""
链接：https://www.matiji.net/exam/brushquestion/91/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
思路：先对每个松鼠的期望值排序，从小到大
     然后求出sum(期望)和瓜子数m的大小
        - 如果sum(期望)小于瓜子数，那么直接输出0
        - 如果sum(期望)大于瓜子数，那么求出两者的差add
     将add平均分配到每个松鼠身上，然后求平和之和即可
"""
import sys
import os


def main():
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    # print(nums)
    # print("sum(nums):", sum(nums))
    add = sum(nums) - m
    if add <= 0:
        print(0)
        return
    res = [0 for _ in range(n)]
    while True:
        for x in range(n):
            if add <= 0:
                break
            res[x] += 1
            add -= 1
        if add <= 0:
            break
    xxx = 0
    for re in res:
        xxx += re * re
    print(xxx)


if __name__ == '__main__':
    main()
