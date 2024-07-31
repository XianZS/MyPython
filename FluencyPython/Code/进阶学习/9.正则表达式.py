"""
    main1():Use re.match()
        mean:从b的头部开始，如果a位于b的头部，则返回相关信息，反之，返回None
        xxx=re.match(a,b)
        if success:
            return <re.Match object; span=(index_begin,index_end), match=匹配规则>
            - xxx.span() return (index_begin,index_end)
            - xxx.group() return 匹配规则
        else:
            return None
    main2():Use re.search()
        mean:
"""
import sys
import os
import re


def main1():
    """
        头部匹配
    """
    als = "python XianZS Code"
    ans = "python"
    res = re.match(ans, als)
    print(res)
    print(res.span())
    print(res.group())


def main2():
    als = "python XianZS Code"
    ans = "XianZS"
    res = re.search(ans, als)
    print(res)


if __name__ == '__main__':
    main1()
    main2()
