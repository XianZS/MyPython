"""
链接:https://www.matiji.net/exam/brushquestion/69/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：差分
"""


def main():
    nums = list(map(int, input().split()))
    n = len(nums)
    per = [0 for _ in range(n)]
    per[0] = nums[0]
    for x in range(1, n):
        per[x] = nums[x] - nums[x - 1]
    # print(per)
    res = 0
    for x in range(1, n):
        add = 1
        for y in range(x + 1, n):
            if per[x] == per[y]:
                # print(1)
                add += 1
            else:
                break
        if add >= 2:
            res += (add - 2 + 1)
    print(res)
    return 0


if __name__ == '__main__':
    main()
