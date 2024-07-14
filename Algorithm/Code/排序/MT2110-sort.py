"""
链接：https://www.matiji.net/exam/brushquestion/110/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：排序
"""
import sys


def ins():
    return sys.stdin.readline().strip()


def main() -> int:
    nums = list(ins())
    ans = list(ins())
    als = []
    for cho in ans:
        als.append(nums.index(cho))
    # print(als)
    als.sort()
    for cho in als:
        print(nums[cho], end='')
    return 0


if __name__ == '__main__':
    main()
