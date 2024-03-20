visited = [ [ 0 for x in range(51)] for y in range(51)]
answer = 9999999999
def check_dup(a,b, c,d, rectangle, cur_r):
    x = (a+c)/2
    y = (b+d)/2
    for idx , r  in enumerate(rectangle):
        # if cur_r == idx:
        #     continue
        x1,y1,x2,y2 = r
        if x > x1 and x<x2 and y > y1 and y <y2:
            return True
    return False
def find_rect(x,y, rectangle):
    tmp  = []
    for idx, r in enumerate(rectangle):
        (x1, y1, x2, y2) = r
        if (x == x1 or x == x2) and (y >= y1 and y <= y2):
            tmp.append(idx)
        elif (y == y1 or y == y2) and (x >= x1 and x <= x2):
            tmp.append(idx)
    return tmp
def change(x,y, rectangle, cur):
    flag = False
    for idx, r in enumerate(rectangle):
        (x1, y1, x2, y2) = r
        if idx == cur:
            continue
        if (x == x1 or x == x2) and (y >= y1 and y <= y2):
            return idx
        elif (y == y1 or y == y2) and (x >= x1 and x <= x2):
            return idx
    return -1
    
def dfs(x,y, item_x, item_y, cur_r, rectangle, cnt):
    global answer, visited
    if x == item_x and y == item_y:
        answer = min(answer, cnt)
        # print(cnt)
        return 
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited[x][y] = 1
    for i in range(4):
        nx = x+ dx[i]
        ny = y+ dy[i]
        # print(cur_r)
        x1, y1, x2, y2 = rectangle[cur_r]
        # print(rectangle[cur_r])
        if nx < 1 or ny < 1 or nx > 50 or ny > 50 :
            continue
        if visited[nx][ny]:
            continue
        if check_dup(x,y,nx,ny, rectangle, cur_r):
            continue
        if ( (nx == x1 or nx == x2) and (ny >= y1 and ny <= y2) )or ( (ny == y1 or ny == y2) and (nx >= x1 and nx <= x2)):
            new_r = change(nx,ny,rectangle, cur_r)
            if(nx != item_x and ny != item_y):
                visited[nx][ny] = 1
            # print(nx, ny)
            if new_r == -1:
                # print(nx,ny)
                dfs(nx,ny,item_x,item_y,cur_r, rectangle, cnt+1)
            else:
                # print(nx,ny, new_r)
                dfs(nx,ny,item_x,item_y, new_r, rectangle, cnt+1)
def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    curs = find_rect(characterX, characterY, rectangle)
    # print(cur)
    for cur in curs:
        dfs(characterX, characterY, itemX, itemY, cur, rectangle, 0)
    return answer