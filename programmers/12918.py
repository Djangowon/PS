s = str(input())


def solution(s):
    if (len(s) == (4 or 6)) and s.isdigit() is True:
        return True
    else:
        return False


print(solution(s))