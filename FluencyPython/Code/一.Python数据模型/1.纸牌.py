"""
[1] collections.namedtuple魔术方法
基础语法：
    TypeName = collections.namedtuple("TypeName", [成员属性, 成员属性])
"""
import collections

Card = collections.namedtuple("Card", ["id", "name"])


def main():
    nums = []
    card1 = Card(1, "kom")
    card2 = Card(2, "lom")
    card3 = Card(3, "jom")
    nums.extend([card1, card2, card3])
    for cho in nums:
        print(cho.id, " >>> ", cho.name)
    return True


if __name__ == '__main__':
    main()
