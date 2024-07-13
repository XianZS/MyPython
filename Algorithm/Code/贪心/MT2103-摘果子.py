import sys


def ins() -> str:
    return sys.stdin.readline().strip()


def main() -> int:
    n, t = map(int, ins().split())
    ans = list(map(int, ins().split()))
    dns = list(map(int, ins().split()))
    tns = list(map(int, ins().split()))

    return 0


if __name__ == '__main__':
    main()
