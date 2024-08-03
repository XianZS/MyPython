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
        mean:判断b的有没有a这个子串
        xxx=re.search(a,b)
    main3():Use re.findall(匹配规则，被匹配字符串)
        mean:在被匹配字符串中，找出所有符合匹配的信息
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


def main3():
    als = "python some xzs python on somethings"
    ans = "python"
    res = re.findall(ans, als)
    print(res)


if __name__ == '__main__':
    main1()
    print("*********")
    main2()
    print("*********")
    main3()
    print("*********")
