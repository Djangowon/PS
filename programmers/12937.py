'''
Time Complexity: O(1)
'''

num = int(input())


def solution(num):
    if num % 2 == 0:
        return "Even"
    if num % 2 == 1:
        return "Odd"


print(solution(num))