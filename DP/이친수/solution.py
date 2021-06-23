N = int(input())

dp = {1:1, 2:1, 3:2, 4: 3}

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
    
# 1 1 2 3 5

# 1 / 10 11 / 100 101 110 111 / 1000 1001 1010 1011 1100 1101 1110 1111 /
