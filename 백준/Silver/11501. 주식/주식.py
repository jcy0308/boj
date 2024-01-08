t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max = arr[-1]
    for i in range(n-1,-1,-1):
        if arr[i] <= max:
            ans += max - arr[i]
        else:
            max = arr[i]
    print(ans)
        