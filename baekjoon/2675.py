import sys

T = int(sys.stdin.readline())

for _ in range(T):
    S = (list(map(str, sys.stdin.readline().split())))

    ans = []
    for i in S[-1]:
        ans.append(i * int(S[0]))

    print(''.join(ans))
