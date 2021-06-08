from collections import Counter

a = input()
cnt_dict = Counter(a)
stack = []
print(cnt_dict)
for key in cnt_dict:
    print(key)
