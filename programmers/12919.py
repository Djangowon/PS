seoul = list(map(str, input().split()))


def solution(seoul):
    kim = str(seoul.index('Kim'))
    return "김서방은 " + kim + "에 있다"


print(solution(seoul))