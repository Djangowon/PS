x = int(input())


def solution(x):
    F0 = 0
    F1 = 1

    answer = []

    answer.append(F0)
    answer.append(F1)

    while True:
        answer.append(answer[-2]+answer[-1])
        if len(answer) == 100:
            break

    return answer[x]


print(solution(x))


def fibo(x):
    if x <= 1:
        return x
    return fibo(x-1) + fibo(x-2)


print(fibo(x))