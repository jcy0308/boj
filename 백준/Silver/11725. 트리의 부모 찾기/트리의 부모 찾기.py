import sys
sys.setrecursionlimit(100000)
n = int(input())

tree = [[] for x in range(n+1)]
for i in range(n-1):
    s, d = map(int, input().split())
    tree[s].append(d)
    tree[d].append(s)

parents = [ -1 for x in range(n+1)]
parents[1] = 0

def dfs(tree, v):
    for i in tree[v]:
        if parents[i] != -1:
            continue
        parents[i] = v
        dfs(tree, i)
dfs(tree, 1)

for i in range(2,n+1):
    print(parents[i])
