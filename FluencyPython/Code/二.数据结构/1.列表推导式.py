import collections
import array


def main():
    Card = collections.namedtuple("Card", ["id", "name"])
    ids = [x for x in range(1, 5)]
    names = ["hom", "jom", "kom", "lom"]
    als = []
    for cho in ((id, name) for id in ids for name in names):
        als.append(Card(cho[0], cho[1]))
    # print(als)
    for al in als:
        print(al)
    print("ends")
    return True


def main1():
    # "I"代表int
    some = array.array("I", (x for x in range(10)))
    print(some)
    for cho in some:
        print(cho, ":", type(cho))


if __name__ == '__main__':
    main()
    main1()

"""
>>> 输出
Card(id=1, name='hom')
Card(id=1, name='jom')
Card(id=1, name='kom')
Card(id=1, name='lom')
Card(id=2, name='hom')
Card(id=2, name='jom')
Card(id=2, name='kom')
Card(id=2, name='lom')
Card(id=3, name='hom')
Card(id=3, name='jom')
Card(id=3, name='kom')
Card(id=3, name='lom')
Card(id=4, name='hom')
Card(id=4, name='jom')
Card(id=4, name='kom')
Card(id=4, name='lom')
ends
进程已结束,退出代码0
"""
