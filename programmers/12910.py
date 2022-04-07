arr = list(map(int, input().split()))
divisor = int(input())


def solution(arr, divisor):
    answer = []

    for i in sorted(arr):
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        return [-1]

    return answer


print(solution(arr, divisor))


def solution2(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]


print(solution2(arr, divisor))