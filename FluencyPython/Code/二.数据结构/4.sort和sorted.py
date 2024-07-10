import sys
import os
import copy


def main():
    als = [("kom", 32), ("lom", 43), ("jom", 54)]
    new1 = sorted(als, reverse=False, key=lambda x: x[1])
    print(new1)
    als.sort(reverse=False, key=lambda x: x[1])
    new2 = copy.copy(als)
    print(new2)
    return True


if __name__ == '__main__':
    main()
