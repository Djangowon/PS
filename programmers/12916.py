s = input()


def solution(s):
    p_count = 0
    y_count = 0

    s = list(s)

    for i in s:
        if (i == 'P') or (i == 'p'):
            p_count += 1
        if (i == 'Y') or (i == 'y'):
            y_count += 1

    if p_count == y_count:
        return True
    else:
        return False


print(solution(s))


def solution2(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution2(s))