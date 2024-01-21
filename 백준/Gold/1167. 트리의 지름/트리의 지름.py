import sys
sys.setrecursionlimit(10**9)
n = int(input())

arr =[]
tree = [[] for i in range(n+1)]
for i in range(1, n+1):
    tmp = (list(map(int, input().split())))
    cnt = 1
    v = tmp[0]
    while tmp[cnt] != -1:
        tree[v].append((tmp[cnt], tmp[cnt+1]))
        cnt += 2
visited = [-1 for i in range(n+1)]
ans = -1
def dfs(tree, v):
    global ans,visited
    idx = -1
    for next, w in tree[v]:
        if visited[next] == -1:
            visited[next] = visited[v] + w
            dfs(tree, next)
visited[2] = 0
dfs(tree, 2)

start = visited.index(max(visited))
visited = [-1 for i in range(n+1)]
visited[start] = 0
dfs(tree, start)
# print(visited)
print(max(visited))