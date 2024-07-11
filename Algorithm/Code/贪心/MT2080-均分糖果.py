"""
链接：https://www.matiji.net/exam/brushquestion/80/3181/1DC60EA6DF83A333301CFFE1407FBA59
算法：贪心
思路：(1)先求原数组的差分数组nums
     (2)collections.deque(差分数组)，这样迭代是为了popleft()
     (3)前提：必然有一个节点只能朝某个方向索取/提交
     (4)设置res来记录最后的结果，设置now来记录每种情况对应的结果
     (5)每次popleft头节点，形成一个新差分数组new，这样做是为了遍历每个节点，让每个节点都作为头节点一次
     (6)从index=0开始，判断当前差分数组new[index]的正负
        - 当new[index]<0时，需要向后面借数字
            newindex for index+1 to n:
            - 当new[newindex]<=0时，pass即可
            - 当new[newindex]>0时
                - 当new[newindex]>abs(new[index])时，表示new[newindex]可以把new[index]的空缺补上
                    new[newindex]-=abs(new[index])
                    now+=(y-x)*new[index]
                    new[index]=0
                - 当new[newindex]<abs(new[index])时，表示new[newindex]不可以把new[index]补上
                    new[index]+=new[newindex]
                    now+=(y-x)*new[newindex]
                    new[newindex]=0
        - 当new[index]>0时，因为new[0 -> index-1]已经被处理过，则证明前面不会再向new[index]借数字，
        所以直接将new[index]置为0，多余出来的数字放到下一位，产生的代价是now+=new[index]
     (7)求得当前情况的代价now之后，取最小数值
     res=min(res,now)
     (8)输出res即可
"""

import math
import collections


def main():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    avg = sum(nums) // n
    res = math.inf
    for x in range(n):
        nums[x] -= avg
    # print(nums)
    nums = collections.deque(nums)
    for _ in range(n):
        now = 0
        xxx = nums.popleft()
        nums.append(xxx)
        # print(nums)
        new = nums.copy()
        for x in range(n):
            if new[x] < 0:
                for y in range(x + 1, n):
                    if new[y] > 0:
                        if new[y] >= abs(new[x]):
                            new[y] -= abs(new[x])
                            now += (y - x) * abs(new[x])
                            new[x] = 0
                            break
                        else:
                            new[x] += new[y]
                            now += (y - x) * new[y]
                            new[y] = 0
            elif new[x] > 0:
                new[x + 1] += new[x]
                now += new[x]
                new[x] = 0
            # print(new, now)
        res = min(res, now)
        # print("***************************")
    print(res)
    return 0


if __name__ == '__main__':
    main()
