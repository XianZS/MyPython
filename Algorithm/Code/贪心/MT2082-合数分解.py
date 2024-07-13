"""
链接：https://www.matiji.net/exam/brushquestion/82/3181/1DC60EA6DF83A333301CFFE1407FBA59?from=1
算法：贪心+数论
"""
import sys
import os


def judge(number):
    mod = number % 4
    count = number // 4
    res = 0
    if mod == 0:
        res = count
    elif mod == 1:
        if count >= 2:
            res = count - 2 + 1
        else:
            res = -1
    elif mod == 2:
        if count >= 1:
            res = count - 1 + 1
        else:
            res = -1
    elif mod == 3:
        if count >= 3:
            res = count - 3 + 2
        else:
            res = -1
    return res


def main():
    c = int(input())
    for _ in range(c):
        number = int(input())
        count = judge(number)
        print(count)
    return 0


if __name__ == '__main__':
    main()
