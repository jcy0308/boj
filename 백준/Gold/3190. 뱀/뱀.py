from collections import deque
n = int(input())
board = [[-1 for x in range(n+1)] for y in range(n+1)]
k = int(input())
for i in range(k):
    x,y = map(int, input().split())
    board[x][y] = 5
    
def move(x,y):
    global board
    dir = board[x][y]
    if dir == 0:
        x -= 1
    elif dir == 1:
        y += 1
    elif dir ==2:
        x += 1
    elif dir == 3:
        y -= 1
    return x,y
    

t = int(input())
h_x, h_y  = 1,1
t_x, t_y = 1,1
board[1][1] = 1
q = deque()
for _ in range(t):
    time, dir = input().split()
    q.append([int(time), dir])
time  = 0
cur_dir = 1
while True:
    time += 1
    if cur_dir == 0:
        h_x -= 1
        if h_x < 1:
            break
        if board[h_x][h_y] == -1:
            tmpx, tmpy = t_x, t_y
            t_x, t_y = move(t_x, t_y)
            board[tmpx][tmpy] = -1
        elif board[h_x][h_y] in [0,1,2,3]:
            break
    elif cur_dir == 1:
        h_y += 1
        if h_y > n:
            break
        if board[h_x][h_y] == -1:
            tmpx, tmpy = t_x, t_y
            t_x, t_y = move(t_x, t_y)
            board[tmpx][tmpy] = -1
        elif board[h_x][h_y] in [0,1,2,3]:
            break
    elif cur_dir == 2:
        h_x += 1
        if h_x > n:
            break
        if board[h_x][h_y] == -1:
            tmpx, tmpy = t_x, t_y
            t_x, t_y = move(t_x, t_y)
            board[tmpx][tmpy] = -1
        elif board[h_x][h_y] in [0,1,2,3]:
            break
    elif cur_dir == 3:
        h_y -= 1
        if h_y < 1:
            break
        if board[h_x][h_y] == -1:
            tmpx, tmpy = t_x, t_y
            t_x, t_y = move(t_x, t_y)
            board[tmpx][tmpy] = -1
        elif board[h_x][h_y] in [0,1,2,3]:
            break

    board[h_x][h_y] = cur_dir 

    # if board[h_x][h_y] == -
    # t_x, t_y = move(t_x, t_y)
    # h_x, h_y = move(h_x, h_y)
    if h_x < 1 or h_x > n or h_y < 1 or h_y > n:
        break
        # print([h_x,h_y], [t_x,t_y])
    # print([h_x,h_y], [t_x,t_y])
    # time += 1
    if q and q[0][0] == time:
        # print('t')
        t, dir = q.popleft()
        if dir == 'L': #반시계
            cur_dir = (cur_dir + 3) %4
        elif dir == 'D':
            cur_dir = (cur_dir +1) % 4
        
        board[h_x][h_y] = cur_dir
# print()
# for i in range(1,n+1):
#     print(board[i][1:])
print(time)