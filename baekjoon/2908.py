A, B = list(map(int, input().split()))

A = str(A)[::-1]
B = str(B)[::-1]

print(max(A, B))