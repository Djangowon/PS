'''
Time Complexity: O(len(...))
'''

n = int(input())


def solution(n):
    a = list(str(int(n)))
    a.sort(reverse=True)
    answer = int(''.join(a))

    return answer


# def solution(n):
#     a = list(map(int, (str(n))))
#     a.sort(reverse=True)
#     answer = int(''.join(str(_) for _ in a))
#
#     return answer


print(solution(n))
