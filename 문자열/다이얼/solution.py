a = input()
answer = 0

for c in a:
    if c in ["A", "B", "C"]:
        answer += 3
    elif c in ["D", "E", "F"]:
        answer += 4
    elif c in ["G", "H", "I"]:
        answer += 5
    elif c in ["J", "K", "L"]:
        answer += 6
    elif c in ["M", "N", "O"]:
        answer += 7
    elif c in ["P", "Q", "R", "S"]:
        answer += 8
    elif c in ["T", "U", "V"]:
        answer += 9
    elif c in ["W", "X", "Y", "Z"]:
        answer += 10

print(answer)


# 더 나은 풀이 출처 https://taiyakee.tistory.com/74
a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
b = input()
sum = 0
for x in b:
    for idx, val in enumerate(a):
        if x in val:
            sum += (idx+3)
print(sum)