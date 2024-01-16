n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = []
dp.append([0,arr[0],arr[0]])
for i in range(1,n):
    dp.append([max(dp[i-1][0],dp[i-1][1],dp[i-1][2]), dp[i-1][0]+arr[i], dp[i-1][1]+arr[i]])

print(max(dp[n-1]))