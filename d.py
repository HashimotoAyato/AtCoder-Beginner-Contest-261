import numpy as np

N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = np.zeros(5000+1, int)
for i in range(M):
    cy = list(map(int, input().split()))
    Y[cy[0]] = cy[1]

# i番目のコイントスでカウントjのときの金額の最大値
dp = np.zeros((N+1,N+1), int)

for i in range(1,N+1):
    # i番目のコイントスで裏が出た場合
    dp[i,0] = np.max(dp[i-1,:])
    for j in range(1,i+1):
        dp[i,j] = dp[i-1, j-1] + X[i-1] + Y[j]

print(np.max(dp[N,:]))