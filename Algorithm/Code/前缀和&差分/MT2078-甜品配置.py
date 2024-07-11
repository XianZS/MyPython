import collections


def main():
    v, n, m = map(int, input().split())
    one = collections.namedtuple("one", ["value", "price"])
    als = []
    for _ in range(n):
        a, b = map(int, input().split())
        als.append(one(value=a, price=b))
    some = sorted(als, key=lambda x: x.value)
    # print(some)
    # for cho in some:
    #     print(cho)
    L = 0
    R = n - 1
    res = 0
    while L <= R:
        mid = (L + R) // 2
        if m & 1:
            new = some[mid - m // 2:mid + m // 2 + 1]
            number = sum([x.price for x in new])
            if number <= v:
                res = some[mid].value
                L = mid + 1
            else:
                R = mid - 1
        else:
            new = some[mid - (m - 1) // 2:mid + m // 2 + 1]
            number = sum([x.price for x in new])
            if number <= v:
                res = (some[mid].value + some[mid + 1].price) // 2
                L = mid + 1
            else:
                R = mid - 1
    print(res)
    return 0


if __name__ == '__main__':
    main()
