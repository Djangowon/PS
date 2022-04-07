n = int(input())


def solution(n):
    s = "수박"
    answer = ''

    if n % 2 == 0:
        answer = s * (n // 2)
    elif n % 2 != 0:
        answer = s * (n // 2) + "수"

    return answer


print(solution(n))


def solution2(n):
    return "수박" * (n // 2) + "수" * (n % 2)


print(solution2(n))

