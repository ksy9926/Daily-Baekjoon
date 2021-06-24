# DFS 문제의 경우 깊이의 제한의 default로 파이선은 1000이므로 많은 data의 경우 값이 안나올 수 있다.
import sys
sys.setrecursionlimit(10**8)

def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        else:
            if graph[x][y] == 1:
                graph[x][y] = 0
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                dfs(x-1, y-1)
                dfs(x+1, y-1)
                dfs(x-1, y+1)
                dfs(x+1, y+1)
                return True
            else:
                return False

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []

    for i in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1

    print(result) 