"""
内容:给定一个𝑁∗𝑀,N∗M的矩阵，1表示已经占用了，0表示没有被占用，求一个由0构成的矩阵，使其周长最大。
答案:最大周长
链接:https://www.matiji.net/exam/brushquestion/51/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法:前缀和+暴力
"""
import sys
import sys


def main():
    n, m = map(int, input().split())
    nums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp = []
    for _ in range(n):
        dp.append(list(map(int, input())))
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            nums[x][y] = dp[x - 1][y - 1] + nums[x - 1][y] + nums[x][y - 1] - nums[x - 1][y - 1]
    res = 1
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            for z in range(x, n + 1):
                for w in range(y, m + 1):
                    if nums[z][w] - nums[z][y - 1] - nums[x - 1][w] + nums[x - 1][y - 1] == 0:
                        res = max(res, (z - x + 1 + w - y + 1) * 2)
    print(res)


if __name__ == "__main__":
    main()
