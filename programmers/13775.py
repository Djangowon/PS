L = list(map(int, input().split()))
x = int(input())


def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1

    while lower <= upper:
        middle = (lower + upper) //2
        if L[middle] == x:
            idx = L.index(x)
            break

        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle -1
    return idx


print(solution(L, x))
