"""
https://www.acwing.com/problem/content/25/
"""


class Solution(object):
    def NumberOf1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n == 0:
            return 0
        if n > 0:
            while n:
                if n & 1:
                    res += 1
                n >>= 1
            return res
        number = int(pow(2, 32))
        n = number + n
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res
