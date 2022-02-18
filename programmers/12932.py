'''
Time Complexity: O(n)
'''

n = int(input())


def solution(n):
    answer = []
    a = list(str(n))

    for i in a:
        answer.append(int(i))

    answer.reverse()

    return answer


print(solution(n))


def digit_reverse(n):
    return list(map(int, reversed(str(n))))


print(digit_reverse(n))
