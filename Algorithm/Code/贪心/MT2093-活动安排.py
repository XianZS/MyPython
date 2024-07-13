"""
链接：https://www.matiji.net/exam/brushquestion/93/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
思路：排序优先级为“结束时间”
判断下一个活动的开始时间，是否大于等于当前记录的结束时间
"""
import sys

input = lambda: sys.stdin.readline().strip()


def main() -> int:
    n = int(input())
    als = [list(map(int, input().split())) for _ in range(n)]
    als.sort(key=lambda xxx: xxx[1])
    res = 0
    time = 0
    for begin, end in als:
        if begin >= time:
            res += 1
            time = end
    print(res)
    return 0


if __name__ == '__main__':
    main()
