'''
Time Complexity: O(1)
'''

n = int(input())
m = int(input())


def solution(n, m):
    answer = []

    for i in range(min(n, m), 0, -1):
        if n % m == 0 and m % n == 0:
            answer.append(i)
            pass

    for i in range(max(n, m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            pass

    return answer


print(solution(n, m))