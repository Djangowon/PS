strings = list(map(str, input().split()))
n = int(input())


def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x[0:]))


print(solution(strings, n))