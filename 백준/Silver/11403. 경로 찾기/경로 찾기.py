n = int(input())
arr = [[9999 for _ in range(n+1)] for __ in range(n+1)]
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    for j in range(1,n+1):
        arr[i][j] = min(arr[i][j], tmp[j-1])

for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if arr[j][i] == 1 and arr[i][k] == 1:
                arr[j][k] = 1

for i in range(1, n+1):
    print(*arr[i][1:])
    