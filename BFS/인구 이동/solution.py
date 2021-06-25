from collections import deque
# (1 <= N <= 50, 1 <= L <= R <= 100)
N, L, R = map(int, input().split())

graph = [0*N for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
change = True

def bfs(x, y):
    q = deque()
    union = []
    visited = []
    q.append((x, y))
    union.append((x, y))
    visited.append((x, y))
    total, p = graph[x][y], 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    total += graph[nx][ny]
                    p += 1
                    union.append((nx, ny))
                    visited.append((nx, ny))
                    q.append((nx, ny))
                
    if p != 1:
            global answer
            global change
            answer += 1
            change = True
    else:
        global change
        change = False
    for a in union:
        graph[a[0]][a[1]] = total // p

while change == True:
    for i in range(N):
        for j in range(N):
            bfs(i, j)

print(graph)
print(answer)
