N = int(input())


count = 0
new_num = N


while True:
    a = new_num // 10
    b = new_num % 10
    c = (a + b) % 10
    new_num = (b * 10) + c

    count += 1
    if new_num == N:
        break


print(count)
