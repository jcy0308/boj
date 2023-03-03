import sys
from collections import deque

def input():
    return sys.stdin.readline()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []
n=int(input())

array = [[0 for x in range(n)] for y in range(n)]
visited = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    tmp=input()
    for j in range(n):
        array[i][j] = int(tmp[j])

que = deque()
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and array[i][j] == 1:
            que.append((i,j))
            visited[i][j]=1
            count = 1
            while len(que) != 0:
                (x,y) = que.popleft()
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visited[nx][ny] == 1:
                        continue
                    if array[nx][ny] == 1:
                        visited[nx][ny] = 1
                        count += 1
                        que.append((nx,ny))
            ans.append(count)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])