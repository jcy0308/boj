from collections import deque
arr = []
for i in range(12):
    arr.append(list(input()))
mark = [[0 for _ in range(6)] for __ in range(12)]
answer = 0
def dfs_all(arr):
    delta = [[1,0],[-1,0],[0,1],[0,-1]]
    dist = [[-1 for _ in range(6)] for __ in range(12)]
    cnt = 0
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.':
                continue
            if dist[i][j] != -1:
                continue
            q = deque()
            q.append((i,j,arr[i][j]))
            dist[i][j] = 0
            tmplist = [(i,j)]
            while q:
                cur = q.popleft()
                for k in range(4):
                    nx = cur[0] + delta[k][0]
                    ny = cur[1] + delta[k][1]
                    color = cur[2]
                    if nx < 0 or nx >= 12 or ny < 0 or ny >=6:
                        continue
                    if dist[nx][ny] != -1:
                        continue
                    if arr[nx][ny] != color:
                        continue
                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1
                    q.append((nx,ny,color))
                    tmplist.append((nx,ny))
            if len(tmplist) >= 4:
                for item in tmplist:
                    mark[item[0]][item[1]] = 1
                cnt += 1
    # for i in range(12):
    #     print(mark[i])
    return cnt
def reorder(arr):
    for i in range(6):
        tmp = deque()
        cnt = 0
        for j in range(11, -1, -1):
            if mark[j][i] == 1:
                cnt += 1
            elif mark[j][i] == 0 and arr[j][i] != '.':
                tmp.append((arr[j][i],cnt))
        for j in range(11,-1,-1):
            if tmp:
                arr[j][i] = tmp.popleft()[0]
            else:
                arr[j][i] = '.'
    # for i in range(12):
    #     print(arr[i])
    # print()
    return

def clear():
    for i in range(12):
        for j in range(6):
            mark[i][j] = 0

while dfs_all(arr):
    answer += 1
    reorder(arr)
    clear()

# dfs_all(arr)
# reorder(arr)
# clear()
print(answer)