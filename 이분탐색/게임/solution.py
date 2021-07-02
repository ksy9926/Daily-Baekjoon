X, Y = map(int, input().split())

p = int(Y*100/X)
start, end = 0, 1000000000
result = 0

if p >= 99:
    print(-1)
    exit()

while start <= end:
    mid = (start+end)//2
    if int((Y+mid)*100/(X+mid)) > p:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)