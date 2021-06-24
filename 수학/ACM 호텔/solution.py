T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    answer = ""
    answer += str(N % H) if N % H != 0 else str(H)
    if (N-1) // H >= 9:
        answer += str((N-1)//H + 1)
    else:
        answer += "0" + str((N-1)//H + 1)
    print(answer)