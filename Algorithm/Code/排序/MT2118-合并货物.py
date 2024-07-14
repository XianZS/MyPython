"""
链接：https://www.matiji.net/exam/brushquestion/118/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：排序
"""
import sys
import collections


def ins():
    return sys.stdin.readline().strip()


def main():
    n = int(ins())
    nums = list(map(int, ins().split()))
    res = 0
    while n != 1:
        nums.sort(reverse=True)
        a = nums.pop()
        b = nums.pop()
        temp = a + b
        nums.append(temp)
        res += temp
        n -= 1
    print(res)


if __name__ == '__main__':
    main()
