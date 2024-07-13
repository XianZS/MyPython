"""
链接:https://www.matiji.net/exam/brushquestion/96/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法:贪心
思路:从前向后,一段不行就下一段
"""
import sys


def ins() -> str:
    return sys.stdin.readline().strip()


def main() -> int:
    n, m = map(int, ins().split())
    nums = list(map(int, ins().split()))
    # print(nums)
    res = 0
    number = 0
    for x in range(n):
        if number + nums[x] <= m:
            number += nums[x]
        else:
            number = nums[x]
            res += 1
    print(res + 1)
    return 0


if __name__ == '__main__':
    main()
