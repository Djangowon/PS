n = int(input())


def solution(n):
    return min([i for i in range(2, n + 1) if n % i == 1])


print(solution(n))

