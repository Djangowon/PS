import sys

N = int(sys.stdin.readline())

for _ in range(N):
    T = str(sys.stdin.readline())
    score = 0
    count = 0

    for i in T:
        if i == 'O':
            count += 1
            score += count
        elif i == 'X':
            count = 0

    print(score)




