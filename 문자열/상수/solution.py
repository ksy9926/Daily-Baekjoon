a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
a = int("".join(a))
b = int("".join(b))
print(a) if a>b else print(b)


# 간단한 형태
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(a) if a>b else print(b)