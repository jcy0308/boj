from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n = int(input())
board = []
visited = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))

def bfs(h):
    global board,n, visited
    cnt = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if board[i][j] <= h:
                continue
            visited[i][j] = 1
            q.append([i,j])
            cnt +=1
            while q:
                cur = q.popleft()
                for k in range(4):
                    nx,ny = cur[0]+dx[k], cur[1]+dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if visited[nx][ny]:
                        continue
                    if board[nx][ny] <= h:
                        continue
                    visited[nx][ny] = 1
                    q.append([nx,ny])
    return cnt
def clear():
    global visited
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
ans = 0
for i in range(0,101):
    tmp = bfs(i)
    # print(tmp)
    if tmp > ans:
        ans = tmp
    clear()
print(ans)
                    
