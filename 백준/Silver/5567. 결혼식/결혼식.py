from collections import deque
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# for _ in range(n+1):
#     print(arr)
cnt = 0
q= deque()
visited = [0 for x in range(n+1)]
visited[1] = 1
if len(arr[1]) == 0:
    print(0)
    exit()
q.append(1)
while q:
    cur = q.popleft()
    for node in arr[cur]:
        if visited[node]:
            continue
        visited[node] = visited[cur] + 1
        q.append(node)
        if visited[node] <= 3:
            cnt +=1

# print(visited)
print(cnt)