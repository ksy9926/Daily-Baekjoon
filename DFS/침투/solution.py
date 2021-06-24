# DFS 문제의 경우 깊이의 제한의 default로 파이썬은 1000이므로 많은 data의 경우 값이 안나올 수 있다.
import sys
sys.setrecursionlimit(10**8)

M, N = map(int, input().split())

graph = []

# 그래프 그리기
for i in range(M):
    graph.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs 함수
def dfs(x, y):
    if 0 <= x < M and 0 <= y < N:
        if graph[x][y] == 0:
            graph[x][y] = 2
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)

# 첫 줄 기준 dfs
for i in range(N):
    if graph[0][i] == 0:
        dfs(0, i)
    
# 조건에 맞는게 없을 경우 NO
if 2 in graph[-1]:
    print("YES")
else:
    print("NO")




## deque 풀이 출처 https://jinho-study.tistory.com/900
from collections import deque
def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 2
    while q:
        y, x = q.popleft()    
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
                q.append((Y, X))
                graph[Y][X] = 2
            
M, N = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for j in range(N):
    if graph[0][j] == 0:
        bfs(0, j)
print("YES" if 2 in graph[-1] else "NO")