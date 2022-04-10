n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x: x[0])
arr = sorted(arr, key = lambda x: x[1])

last = 0
count = 0

for i, j in arr:
    if i >= last:
        count += 1
        last = j


print(count)