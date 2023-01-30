import sys
from collections import deque
input = sys.stdin.readline
delta = [[1,0], [-1,0], [0,1], [0,-1]]
m, n, k = map(int, input().split())
arr = [[1 for x in range(n)] for y in range(m)]
visited = [[0 for x in range(n)] for y in range(m)]
# print(visited)
for i in range(k):
    x1, y1, x2, y2 = map(int ,input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[m-y-1][x] = 0

# print(visited)
que = deque()
ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j] and not visited[i][j] :
            visited[i][j] = 1
            que.append([i,j])
            tmp_cnt = 0
            # print('starting', i,j)
            while len(que):
                cur = que.popleft()
                tmp_cnt += 1
                # print('cur = ', cur)
                for k in range(4):
                    new = [cur[0]+delta[k][0], cur[1]+delta[k][1]]
                    # print('new = ', new)
                    if new[0] < 0 or new[0] >= m or new[1] < 0 or new[1] >= n:
                        continue
                    if visited[new[0]][new[1]] == 1 or arr[new[0]][new[1]] == 0:
                        continue
                    visited[new[0]][new[1]] = 1
                    que.append(new)
                    # print('appending =', new)
                    
            ans.append(tmp_cnt)
print(len(ans))
for item in sorted(ans):
    print(item, end= ' ')
                
        