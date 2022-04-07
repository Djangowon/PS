price, money, count = map(int, input().split())


def solution(price, money, count):
    total = 0

    for i in range(1, count + 1):
        total += price * i

    if money >= total:
        return 0

    return total - money


print(solution(price, money, count))


def solution2(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)


print(solution2(price, money, count))