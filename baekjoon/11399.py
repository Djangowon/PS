'''
Time Complexity: O(n)
'''

N = int(input())
P = list(map(int, input().split()))
P.sort()

result = 0
prefix_sum = [0]

for i in range(len(P)):
    prefix_sum.append(P[i]+prefix_sum[i])

for i in prefix_sum:
    result += i

print(result)