import sys

n = int(sys.stdin.readline())
a = (list(map(int, sys.stdin.readline().split())))


def solve(a):
    return sum(a)


print(solve(a))