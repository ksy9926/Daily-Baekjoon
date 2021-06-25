from collections import deque
# (1 <= N <= 50, 1 <= L <= R <= 100)
N, L, R = map(int, input().split())

graph = [0*N for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
q = deque()

def bfs(x, y):
    global check
    q.append((x, y))
    visited[x][y] = True
    s = graph[x][y]
    union = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    check = True
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    s += graph[nx][ny]
    for a, b in union:
        graph[a][b] = s // len(union)
                
while True:
    visited = [[False] * N for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                bfs(i, j)
    if check:
        answer += 1
    else:
        break

print(answer)



# https://javaiyagi.tistory.com/614 참고