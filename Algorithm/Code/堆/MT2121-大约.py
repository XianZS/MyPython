"""
链接：https://www.matiji.net/exam/brushquestion/121/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：堆+双指针
题目：给你一个相邻数差不超过 1 的序列，求最长子串的长度，满足子串中的最大值减最小值也不超过 1
思路：不断更新当前区间的范围，最大值和最小值，取最大值即可
"""

import sys
import collections


def ins() -> str:
    return sys.stdin.readline().strip()


def main() -> int:
    n = int(ins())
    nums = list(map(int, ins().split()))
    if n == 2:
        print(1)
    res = 1
    new = collections.deque([nums[0], nums[1]])
    count = 2
    for x in range(2, n):
        new.append(nums[x])
        count += 1
        min_num = min(new)
        max_num = max(new)
        while max_num - min_num > 1:
            new.popleft()
            count -= 1
            if len(new) == 0:
                count = 0
                break
            min_num = min(new)
            max_num = max(new)
        res = max(res, count)
    print(res, end='')
    return 0


if __name__ == '__main__':
    main()
