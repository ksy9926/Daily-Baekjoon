N = int(input())

move = []

def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)

hanoi(N, 1, 2, 3)

print(len(move))

for i in range(len(move)):
    print(f'{move[i][0]} {move[i][1]}')


# 1개  -> 1회
# 2개 ->  3회 (1*2 + 1)
# 3개 -> 7회 (3*2 + 1)
# 4개 -> 15회 (4*2 + 1)

# 1개
# 1 3

# 2개
# 1 2

# 1 3
# 2 3

# 3개
# 1 3

# 1 2
# 3 2

# 1 3
# 2 1
# 2 3
# 1 3

# 4개
# 1 2

# 1 3
# 2 3

# 1 2
# 3 1
# 3 2
# 1 2

# 1 3
# 2 3
# 2 1
# 3 1
# 2 3
# 1 2
# 1 3
# 2 3