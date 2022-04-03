'''
Time Complexity: O(n)
'''

phone_number = input()


def solution(phone_number):
    blind_words = []
    words = phone_number[:-4]
    for i in words:
        blind_words.append('*')

    four_words = phone_number[-4:]

    return "".join(blind_words) + str(four_words)


print(solution(phone_number))


def solution2(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]

print(solution2(phone_number))