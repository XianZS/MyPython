import sys


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    res = 0
    now = nums[0]
    for x in range(1, n):
        res += now
        now += nums[x]
    # print(res)
    print("%.2f" % (res / n))


if __name__ == '__main__':
    main()
