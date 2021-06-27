N = int(input())

exist = False

for i in range(1, N+1):
    s = 0
    for num in list(str(i)):
        s += int(num)
    result = i + s
    if result == N:
        print(i)
        exist = True
        break

if exist == False:
    print(0)