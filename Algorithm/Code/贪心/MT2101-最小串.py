"""
链接：https://www.matiji.net/exam/brushquestion/101/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
题目：给定一个由0， 1，2 组成的字符串S。可以交换相邻0， 1或1， 2的位置（例如：12 - 21 ； 01 - 10）
请输出原字符串经过任意转换后字典序最小的字符串。
思路：去掉原数组中所有的1，记录1的个数count
然后输出新数组，在输出新数组的第一个2时，将"1"*count输出，然后继续输出即可
"""
import sys


def ins():
    return sys.stdin.readline().strip()


def main() -> int:
    nums = list(map(int, ins()))
    # print(nums)
    n = len(nums)
    new = []
    count = 0
    for x in range(n):
        if nums[x] != 1:
            new.append(nums[x])
        else:
            count += 1
    judge = 1
    for cho in new:
        if cho == 2 and judge:
            print("1" * count, end='')
            judge = 0
        print(cho, end='')

    return 0


if __name__ == '__main__':
    main()
