# sizes = [list(map(int, input().split())) for _ in range(4)]
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]


def solution(sizes):

    for i in sizes:
        i[0], i[1] = max(i[0], i[1]), min(i[0], i[1])

    return max(sizes, key= lambda x: x[0])[0] * max(sizes, key=lambda x: x[1])[1]


print(solution(sizes))


def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


print(solution2(sizes))