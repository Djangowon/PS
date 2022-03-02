'''
Time Complexity: O(n)
'''

arr = [1,2,3,4]


def solution(arr):
    result = 0

    for i in arr:
        result += i

    answer = result / len(arr)

    return answer


print(solution(arr))
