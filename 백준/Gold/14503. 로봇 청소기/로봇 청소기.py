import sys
sys.setrecursionlimit(10**9)
n,m = map(int, input().split())
x,y,d = map(int, input().split())
arr = []
ans = 0
delta = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(n):
    arr.append(list(map(int, input().split())))
dist = [arr_[:]  for arr_ in arr]
def debug():
    for i in range(n):
        print(dist[i])
    print()
def dfs(x,y,dir):
    global ans
    global arr
    global dist
    flag = False
    if arr[x][y] == 0 and dist[x][y] == 0:
        ans += 1
        dist[x][y] = 2
    for i in range(4):
        nx,ny = x+delta[i][0], y+delta[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny>= m:
            continue
        if dist[nx][ny] == 0:
            flag = True
            break
    if flag == True:
        tx, ty = x,y
        if dir == 0:
            dir = 3
            ty -= 1
        elif dir == 1:
            dir = 0
            tx -= 1
        elif dir == 2:
            dir = 1
            ty += 1
        elif dir == 3:
            dir = 2
            tx += 1
        if tx >= 0 and tx < n and ty >=0 and ty < m and dist[tx][ty] == 0:
            # print(tx,ty,dir)
            dfs(tx,ty, dir)
        else:
            dfs(x,y,dir)
    else:
        # print(dir)
        tx, ty = x,y
        if dir == 0:
            tx += 1 
        elif dir == 1:
            ty -= 1
        elif dir == 2:
            tx -= 1
        elif dir == 3:
            ty += 1
        if tx >= 0 and tx < n and ty >=0 and ty < m and arr[tx][ty] != 1:
            # print("back:", tx, ty)
            dfs(tx,ty,dir)
        else:
            # print(x,y,dir)
            return               
dfs(x,y,d)
print(ans)
# debug()
