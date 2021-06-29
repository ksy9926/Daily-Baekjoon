N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(input()))

chess = [["" for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            chess[i][j] = "W"
        else:
            chess[i][j] = "B"

stack = []

for c in range(N-7):
    for d in range(M-7):
        answer = 0
        another = 0
        for i in range(c, c+8):
            for j in range(d, d+8):
                if graph[i][j] != chess[i][j]:
                    answer += 1
                else:
                    another += 1
        stack.append(min(answer, another))

print(min(stack))