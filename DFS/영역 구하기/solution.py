n, m, k = map(int, input().split())

graph = [[0 for i in range(m)] for j in range(n)]

for _ in range(k):
    squre = list(map(int, input().split()))
    for i in range(len(square)):
        graph[square[i]]