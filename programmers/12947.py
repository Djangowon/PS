'''
Time Complexity: O(n)
'''

x = int(input())


def solution(x):
    num_list = list(map(int, str(x)))
    result = 0
    for i in num_list:
        result += i

    if x % result == 0:
        return True
    else:
        return False


print(solution(x))