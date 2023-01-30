import sys

def input():
    return sys.stdin.readline()

n = int(input())
arr = list(map(int,input().split()))

ans = [0]
for num in arr:
    # print(ans)
    if num > ans[-1]:
        ans.append(num)
    else:
        l, r = 0, len(ans)
        while l < r:
            mid = (l+r)//2
            if num > ans[mid]:
                l = mid+1
            else:
                r = mid 
        ans[r] = num
print(len(ans)-1)                
