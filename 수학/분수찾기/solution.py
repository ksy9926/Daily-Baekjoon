X = int(input())

#      1   2     3       4        5            6
# 분자 1 /1 2 /3 2 1 /1 2 3 4/ 5 4 3 2 1/ 1 2 3 4 5 6
# 분모 1 /2 1 /1 2 3 /4 3 2 1/ 1 2 3 4 5
#      1  2 3  4 5 6  7 8 9 10

i = 1

while True:
    if X <= i:
        break
    X -= i
    i += 1

if i % 2 == 0:
    print(f"{X}/{i-X+1}")
elif i % 2 == 1:
    print(f"{i-X+1}/{X}")