"""
链接：https://www.matiji.net/exam/brushquestion/97/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
题目：给定长度为n的一个数字，去掉其中k个数字，要求保留下来的数字最小，注意，最后输出时，要去掉前导0
思路：- for _ from 0 -> k:
     # 循环k次，代表去掉k个数字
        - for x from 0 -> n-1:
        # 循环n-1次，每次找出nums[x]>nums[x+1]的情况
            - for y from x -> n-1:
            # 循环，每次将nums[x+1 to n]的数字向前移动一位
            n-=1
            break
"""
import sys


def ins() -> str:
    return sys.stdin.readline().strip()


def main() -> int:
    nums = list(map(int, ins()))
    k = int(ins())
    n = len(nums)
    add = n - k
    for _ in range(k):
        for x in range(n - 1):
            if nums[x] > nums[x + 1]:
                for y in range(x, n - 1):
                    nums[y] = nums[y + 1]
                n -= 1
                break
    res = ""
    for x in range(add):
        res += str(nums[x])
    print(int(res))
    return 0


if __name__ == '__main__':
    main()
