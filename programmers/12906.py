arr = list(map(int, input().split(',')))


def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        elif answer[-1] != i:
            answer.append(i)

    return answer


print(solution(arr))


def solution2(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer


print(solution2(arr))