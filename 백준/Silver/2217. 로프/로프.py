import sys

def input():
    return sys.stdin.readline()

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
last_value = array[-1]
ans = last_value
for i in range(n-1):
    tmp = array[i]*(n-i)
    if tmp > ans:
        ans = tmp

print(ans)