T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [[0] * n for _ in range(k+1)]
    dp[0] = [i+1 for i in range(n)]

    for i in range(1, k+1):
        for j in range(n):
            dp[i][j] = sum(dp[i-1][0:j+1])
    
    # for a in dp:
    #     print(a)

    print(dp[k][n-1])

# 2층 3호에 살려면 1층의 1호부터 3호까지의 사람들의 수의 합만큼 사람들과
# 0층 1호 1명 / 0층 2호 2명 / 0층 3호 3명 / 0층 4호 4명 ...
# 1층 1호 1명 / 1층 2호 3명 / 1층 3호 6명 / 1층 4호 10명
# 2층 1호 1명 / 2층 2호 4명 / 2층 3호 10명 / 2층 4호 20명
# 3층 1호 1명 / 3층 2호 5명 / 3층 3호 15명 / 3층 4호 35명