n,m = map(int, input().split())
arr = []
dp = [[0 for _ in range(n)] for __ in range(m+1)]
for i in range(n):
    arr.append(int(input()))
if arr[0] == 1:
    dp[0][0] = 1
for i in range(1,n):
    if arr[i] == 1:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1,m+1):
    for j in range(i-1,n):
        if j == i-1:
            dp[i][j] = i
        else:
            if arr[j] == 1:
                if i%2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]+1)
            elif arr[j] == 2:
                if i%2 == 1:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# for i in range(m+1):
#     print(dp[i])
ans = 0
for i in range(m+1):
    if dp[i][n-1] > ans:
        ans = dp[i][n-1]
print(ans)