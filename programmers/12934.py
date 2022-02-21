'''
Time Complexity: O(n)
'''

import math

n = int(input())


def solution(n):
    return pow(math.sqrt(n)+1, 2) if int(math.sqrt(n)) == math.sqrt(n) else '-1'


print(solution(n))