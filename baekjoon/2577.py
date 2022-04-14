A = int(input())
B = int(input())
C = int(input())


answer = A * B * C
a_list = list(map(int, str(answer)))

for i in range(0, 10):
    print(a_list.count(i))