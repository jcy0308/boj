import sys

def input():
    return sys.stdin.readline()

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
test = list(map(int, input().split()))

arr.sort()

for item in test:
    l, r = 0, n-1
    ans = 0
    while l <= r:
        if arr[-1] < item or arr[0] > item:
            break
        mid = (l+r)//2
        if item == arr[mid]:    
            ans = 1
            break
        elif item > arr[mid]:
            l = mid + 1  #mid는 index에 없는걸 확인했으므로 mid + 1 부터 탐색 
        else:
            r = mid - 1
    print(ans)

    