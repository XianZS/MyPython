"""
    [1]掌握正则表达式的各类原字符规则
    [2]了解字符串的r标记的作用
"""
import re


def main():
    als = "ll**902*&d^568/a[]12;35-==441"
    """
        res1:找出als所有数字:\d
    """
    res1 = re.findall(r"\d", als)
    print(res1)
    """
        res2:找出特殊字符:\W
    """
    res2 = re.findall(r"\W", als)
    print(res2)
    """
        res3:找出所有目标字符:[]
        x-y:表示找出所有ASCII码位于chr(x)——chr(y)之间的字符
    """
    res3 = re.findall(r"[a-zA-Z]", als)
    print(res3)


def main2():
    """
        匹配一个长度为6-10位的字符串，由数字和字母组成
        ^:匹配字符串开头
        &:匹配字符串结尾
    """
    r = '^[0-9a-zA-Z]{6,10}$'
    strs = input()
    res = re.findall(r, strs)
    print(res)


def main3():
    """
        匹配QQ号，第一位不为0，长度为5-11
    """
    r = '[1-9][0-9]{4,10}'


if __name__ == '__main__':
    main()
    print("*********")
    main2()
