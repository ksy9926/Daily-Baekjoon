from collections import deque

T = int(input())

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    return graph[target[0]][target[1]]
            

for _ in range(T):
    I = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))

    graph = [[0]*I for _ in range(I)]

    move = [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1)]
    
    if now == target:
        print(0)
    else:
        print(bfs(now[0], now[1]))

    