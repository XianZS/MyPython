"""
链接：https://www.matiji.net/exam/brushquestion/95/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
思路：先求出小于int(1e9)的所有斐波拉契数，从后向前判断，如何小于number，则number-=als[x]，res+=1，即可，直至number=0，输出res
"""
import sys


def main() -> int:
    als = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
           46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
           24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
    res = 0
    number = int(sys.stdin.readline().strip())
    n = len(als)
    for x in range(n - 1, -1, -1):
        if als[x] <= number:
            res += 1
            number -= als[x]
        if number == 0:
            break
    print(res)
    return 0


if __name__ == '__main__':
    main()
