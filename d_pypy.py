N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = [0 for i in range(N+1)]
for i in range(M):
    c, y = map(int, input().split())
    Y[c] = y

# i番目のコイントスでカウントjのときの金額の最大値
dp = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    # i番目のコイントスで裏が出た場合
    dp[i][0] = max(dp[i-1])
    for j in range(1,i+1):
        dp[i][j] = dp[i-1][j-1] + X[i-1] + Y[j]

print(max(dp[N]))