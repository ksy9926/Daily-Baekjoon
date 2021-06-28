T = int(input())

for _ in range(T):
    n = int(input())
    dp = []
    dp.append(list(map(int, input().split())) + [0])
    dp.append(list(map(int, input().split())) + [0])

    for i in range(1, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][-2], dp[1][-2]))

