n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

cnt = 0
for i in range(n-2, -1 , -1):
    tmp = arr[i] - arr[i+1]
    if tmp >= 0 :
        cnt += tmp + 1
        arr[i] = arr[i] - tmp - 1

print(cnt)