import sys

input = sys.stdin.readline
N = int(input())

lines = []
answer = 0

for _ in range(N):
    lines.append(list(map(int, input().split())))

lines = sorted(lines, key=lambda x: (x[0], x[1]))
last = -1000000001
# last = float('-inf')

for line in lines:
    if last > line[0] and line[1] >= last:
        answer += line[1] - last
        last = line[1]
    elif last > line[0] and line[1] < last:
        pass
    else:
        answer += line[1] - line[0]
        last = line[1]

print(answer)