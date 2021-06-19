a = int(input())

i = 1
coefficient = 6
prev = 1

while prev < a:
    prev += coefficient * i # 7 19
    i += 1

print(i)