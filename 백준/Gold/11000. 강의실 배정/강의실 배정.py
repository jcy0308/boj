import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

arr = []
ans = 1
h = []

for _ in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

arr.sort(key = lambda x: (x[0], x[1]))
heappush(h, arr[0][1])
for item in arr[1:]:
    if item[0] < h[0]:
        ans += 1
        heappush(h, item[1])
    else:
        heappop(h)
        heappush(h, item[1])
print(ans)
    