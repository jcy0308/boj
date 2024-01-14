n, m = map(int,(input().split()))
arr = sorted(list(map(int, input().split())))

def check(arr, value):
    global n
    tmp = 0
    for item in arr:
        tmp += item // value
    if tmp >= n:
        return True
    return False
l = 0
r = 99999999999
while l+1<r:
    mid = (l+r)//2
    if check(arr, mid):
        l = mid 
        # print("l:",l)
    else:
        r = mid
        # print("r:", r)
print(l)