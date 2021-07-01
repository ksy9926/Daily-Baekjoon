N = int(input())

points = []
answer = 0

for _ in range(N):
    points.append(list(map(int, input().split())))

points.sort(key=lambda x: x[1])
points.sort(key=lambda x: x[0])

# 세로 길이 모두 더하기
for i in range(0, N, 2):
    answer += abs(points[i][1] - points[i+1][1])

points.sort(key=lambda x: x[1])

# 가로 길이 모두 더하기
for i in range(0, N, 2):
    answer += abs(points[i][0] - points[i+1][0])

print(answer)
    