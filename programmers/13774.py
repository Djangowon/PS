L = list(map(int, input().split()))
x = int(input())


def solution(L, x):
    answer = [i for i, value in enumerate(L) if value == x]

    if x not in L:
        answer.append(-1)

    return answer


print(solution(L, x))

