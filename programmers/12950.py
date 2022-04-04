'''
Time Complexity: O(n²)
'''


A = [[1,2],[2,3]]
B = [[3,4],[5,6]]


def solution(A, B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A


print(solution(A, B))