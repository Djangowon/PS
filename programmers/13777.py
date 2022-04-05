L = list(map(int, input().split()))
x = int(input())
l = 0
u = 4


def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, mid + 1, u)


print(solution(L, x, l, u))