import sys

n_list = []
for i in range(1, 11):
    n_list.append(int(sys.stdin.readline()))

answer = []

for i in n_list:
    if i % 42 not in answer:
        answer.append(i % 42)

print(len(answer))

