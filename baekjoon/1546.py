import sys

N = int(sys.stdin.readline())
S = (list(map(int, sys.stdin.readline().split())))

new_score = []
for i in S:
    new_score.append((i / max(S)) * 100)

print(sum(new_score) / len(new_score))