from collections import deque

N, M, K = map(int, input().split())

graph = [[0 for i in range(M)] for j in range(N)]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            graph[j][i] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []

def bfs(x, y):
    if graph[x][y] == 0:
        q = deque()
        q.append((x, y))
        w = 1
        graph[x][y] = 2
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                elif graph[nx][ny] == 0:
                    w += 1
                    graph[nx][ny] = 2
                    q.append((nx, ny))
        answer.append(w)

for i in range(N):
    for j in range(M):
        bfs(i,j)

print(len(answer))
answer.sort()
for width in answer:
    print(width, end=" ")