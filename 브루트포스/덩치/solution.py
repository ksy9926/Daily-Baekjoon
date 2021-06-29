N = int(input())

people = []
answer = [1] * N

for _ in range(N):
    people.append(list(map(int, input().split())))

for i in range(len(people)):
    for j in range(len(people)):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            answer[i] += 1

for i in range(N):
    print(answer[i], end=" ") if i != N-1 else print(answer[i])
