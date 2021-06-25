N = int(input())

def star(n):
    if n == 1:
        return ["*"]
    
    cast = star(n//3)

    graph = []

    for s in cast:
        graph.append(s * 3)
    for s in cast:
        graph.append(s + " " * (n//3) + s)
    for s in cast:
        graph.append(s * 3)
    
    return graph

graph = star(N)

for i in range(N):
    for j in range(N):
        print(graph[i][j], end = "")
    print()

# 공간을 1, 2, 3으로 나누어 재귀함수를 통해 구해진 별을 붙인다.
# 출처 https://cotak.tistory.com/38