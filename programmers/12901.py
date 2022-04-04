a = int(input())
b = int(input())


def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b - 1
    for i in range(1, a):
        day += month[i - 1]
    return week[day % 7]


print(solution(a, b))

