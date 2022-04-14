import sys


arr = []

for i in range(1, 10):
    arr.append(list(map(int, sys.stdin.readline().split())))


print(f"{max(arr)[0]}\n{arr.index(max(arr))+1}")