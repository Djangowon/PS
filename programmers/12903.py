import math

s = str(input())


def solution(s):
    answer = []

    if len(s) % 2 != 0:
        answer = s[math.floor(len(s) / 2)]
    elif len(s) % 2 == 0:
        a = math.floor(len(s) / 2)-1
        b = a + 1
        answer = s[a] + s[b]

    return answer


print(solution(s))
