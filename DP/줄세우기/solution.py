# 아직 못 품
 
N = int(input())

children = []

for _ in range(N):
    children.append(int(input()))

dp = [[0]] * N
dp[0] = [children[0]]
print(dp)
answer = 0

for i in range(1, N):
    print(children[i], dp[i-1][-1])
    if children[i] < dp[i-1][-1]:
        answer += 1
    temp = dp[i-1] + [children[i]]
    temp.sort()
    dp[i] = temp

print(children)
print(dp)
print(answer)    