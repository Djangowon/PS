import sys

C = int(sys.stdin.readline())

for _ in range(C):
    N_score = (list(map(int, sys.stdin.readline().split())))
    N = N_score.pop(0)

    AVG = sum(N_score) / N
    answer = 0

    for i in N_score:
        if i > AVG:
            answer += 1

    print("{:.3f}%".format((answer * 100) / N))

