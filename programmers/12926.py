s = str(input())
n = int(input())


def solution(s, n):
    answer = []
    upper = list(range(65, 91))
    lower = list(range(97, 123))
    for i in s:
        if ord(i) == 32:
            answer.append(chr(32))
            continue
        step = ord(i) + n
        if (ord(i) in upper and step > upper[-1]) or (ord(i) in lower and step > lower[-1]):
            answer += chr(step - 26)
        else:
            answer += chr(step)
    return "".join(answer)


print(solution(s, n))


def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)



