a, b = map(int, input().split())


def solution(a, b):
    answer = 0
    for i in range(min(a, b), max(a, b) + 1):
        answer += i
    return answer


print(solution(a, b))


def solution2(a, b):
    if a > b: a, b = b, a

    return sum(range(a, b + 1))


print(solution2(a, b))