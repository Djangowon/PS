a, b, c = map(int, input().split())


# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))


def cash_prize(a, b, c):
    pre = [a, b, c]
    dice = {a, b, c}
    dice = list(set(dice))
    result = 0

    if len(dice) == 1:
        result += max(dice)
        return 10000 + (result * 1000)

    elif len(dice) == 3:
        result += max(dice)
        return result * 100

    elif a == b or b == c or a == c:
        for i in dice:
            pre.remove(i)
        result += pre[0]
        return 1000 + (result * 100)


print(cash_prize(a, b, c))





