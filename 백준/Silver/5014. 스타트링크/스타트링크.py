from collections import deque

f,s,g,u,d = map(int, input().split())
dx = [u,-d]
ans = [-1 for x in range(f+1)]
q = deque()
q.append(s)
ans[s] = 0
while len(q):
    cur = q.popleft()
    for i in range(2):
        nx = cur + dx[i]
        if nx < 1 or nx > f:
            continue
        if ans[nx] != -1:
            continue
        ans[nx] = ans[cur] + 1
        q.append(nx)
if ans[g] == -1:
    print("use the stairs")
else:
    print(ans[g])