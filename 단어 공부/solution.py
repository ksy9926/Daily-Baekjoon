word = input()
word_list = []
word_dict = {}

for s in word:
    s = s.upper()
    if s in word_dict:
        word_dict[s] += 1
    else:
        word_dict[s] = 1

for key, value in word_dict.items():
    word_list.append([key, value])

word_list.sort(key=lambda x: x[1], reverse=True)

if len(word_list) == 1:
    print(word_list[0][0])
elif word_list[0][1] == word_list[1][1]:
    print('?')
else:
    print(word_list[0][0])




# 다른 사람의 풀이
## [출처] 백준 1157번 단어 공부 파이썬|작성자 dingche
n = str(input().upper())
unique = list(set(n))

li = list()
for i in unique:
    li.append(n.count(i))

if li.count(max(li)) > 1:
    print('?')
else:
    temp = li.index(max(li))
    print(unique[temp])
