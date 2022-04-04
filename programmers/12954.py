'''
Time Complexity: O(n)
'''

x = int(input())
n = int(input())


def solution(x, n):
    answer = []
    start = x
    while n != 0:
        answer.append(x)
        x += start
        n -= 1
        continue

    return answer


print(solution(x, n))


def number_generator(x, n):
    return [i * x + x for i in range(n)]


print(number_generator(2, 5))