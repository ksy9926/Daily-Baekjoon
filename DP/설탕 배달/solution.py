a = int(input())
temp = a
answer = 0

while a > 0:
    if a % 5 == 0:
        answer += a // 5
        break
    else:
        a -= 3
        answer += 1

if a % 5 == 0 and a > 0:
    print(answer)
else:
    answer = 0
    a = temp
    while a > 0:
        if a % 3 == 0:
            answer += a // 3
            break
        else:
            a -= 5
            answer += 1
    if a % 3 == 0 and a > 0:
        print(answer)
    else:
        print(-1)