import sys

N = int(sys.stdin.readline())
N_list = int(sys.stdin.readline())

N_list = list(str(N_list))

ans = 0
for i in N_list:
    ans += int(i)

print(ans)

