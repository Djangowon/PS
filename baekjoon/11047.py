N, K = map(int, input().split())
count = 0

A = []

for i in range(1, N+1):
    A.append(int(input()))
    A.sort()
    A.sort(reverse=True)

for i in A:
    count += (K//i)
    K %= i


print(count)

