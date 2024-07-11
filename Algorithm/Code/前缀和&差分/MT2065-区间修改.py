"""
链接：https://www.matiji.net/exam/brushquestion/65/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：差分
注意事项：测试案例有问题
"""

import sys
import os

"""
nums[1]=nums[1]-nums[0]
nums[2]=nums[2]-nums[1]
nums[3]=nums[3]-nums[2]
nums[4]=nums[4]-nums[3]
nums[5]=nums[5]-nums[4]

"""


def main():
    res1, res2 = 0, 0
    n = int(input())
    s = ""
    for x in range(n + 10):
        try:
            s += " " + input()
        except:
            pass
    nums = [0] + list(map(int, s.split()))
    n = len(nums) - 1
    for x in range(2, n + 1):
        number = nums[x] - nums[x - 1]
        if number > 0:
            res1 += number
        else:
            res2 += number
    print(max(res1, -res2))
    return 0


if __name__ == '__main__':
    main()
