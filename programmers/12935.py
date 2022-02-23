'''
Time Complexity: O(n)
'''

arr = [10,9,8,7]


def solution(arr):
    arr.remove(min(arr))

    if len(arr) == 0:
        return [-1]

    return arr


print(solution(arr))