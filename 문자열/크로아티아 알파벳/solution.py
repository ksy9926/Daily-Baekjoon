a = input()
answer = len(a)
dz = 0
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for word in croatia:
    if word in a:
        cnt = a.count(word)
        if word == "dz=":
            dz += cnt
        elif word == "z=":
            cnt -= dz
        answer += cnt * (1 - len(word))

print(answer)



# [출처] [2941] 크로아티아 알파벳 / 파이썬 / 백준 문제 풀이|작성자 망고
a = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in cro:
    a = a.replace(i, "1")
print(len(list(a)))
