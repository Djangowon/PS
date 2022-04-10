# id_list = list(map(str, input().split()))
# report = list(map(str, input().split(',')))
# k = int(input())
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2


def solution(id_list, report, k):
    frozen = []

    list(set(report))

    for i in report:
        if report.count(i.split(' ')[1]) >= k:
            frozen.append(i)

    return frozen


print(solution(id_list, report, k))