import itertools

n,k = map(int, input().split())
top, bot = 1, 1
for i in range(n,n-k,-1):
    top *= i
for i in range(k, 0, -1):
    bot *= i
print(int(top/bot))