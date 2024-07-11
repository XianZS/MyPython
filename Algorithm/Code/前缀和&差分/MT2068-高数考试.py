"""
链接：https://www.matiji.net/exam/brushquestion/68/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：前缀和
"""


def main():
    n, p = map(int, input().split())
    nums = list(map(int, input().split()))
    pre = [0 for _ in range(n)]
    for x in range(n):
        if x == 0:
            pre[x] = nums[x]
        else:
            pre[x] = nums[x] - nums[x - 1]
    for _ in range(p):
        x, y, z = map(int, input().split())
        pre[x - 1] += z
        if y < n:
            pre[y] -= z
    minx = pre[0]
    for x in range(1, n):
        pre[x] += pre[x - 1]
        minx = min(minx, pre[x])
    print(minx)
    return 0


# 2 3 2

if __name__ == '__main__':
    main()
