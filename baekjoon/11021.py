import sys

T = int(sys.stdin.readline())

for i in range(1, T+1):
    A, B = (list(map(int, sys.stdin.readline().split())))
    print(f"Case #{i}: {A+B}")
