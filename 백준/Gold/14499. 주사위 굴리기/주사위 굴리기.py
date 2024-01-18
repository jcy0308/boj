n,m,x,y,k = map(int, input().split())
# dice = [[0 for x in range(3)] for y in range(4)]
dice = [0 for x in range(7)]
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
# print(board)
do = list(map(int, input().split()))
def move(dir):
    global dice
    tmp = dice[:]
    if dir == 1: #동쪽
        dice[6] = tmp[3]
        dice[3] = tmp[1]
        dice[1] = tmp[4]
        dice[4] = tmp[6]
    elif dir == 2: #서쪽
        dice[4] = tmp[1]
        dice[1] = tmp[3]
        dice[3] = tmp[6]
        dice[6] = tmp[4]
    elif dir == 3: #북쪽
        dice[2] = tmp[1]
        dice[1] = tmp[5]
        dice[5] = tmp[6]
        dice[6] = tmp[2]
    elif dir == 4: #남쪽
        dice[2] = tmp[6]
        dice[1] = tmp[2]
        dice[5] = tmp[1]
        dice[6] = tmp[5]
    # print(x,y)
def check(dir):
    global x,y
    curx,cury = x,y
    if dir == 1:
        cury = y+1
    elif dir == 2:
        cury = y-1
    elif dir== 3:
        curx = x-1
    elif dir==4:
        curx = x+1
    if curx <0 or curx>= n or cury<0 or cury >= m:
        # print("oops",x,y)
        return
    x,y = curx,cury
    move(dir)
    if board[x][y] ==0 :
        board[x][y] = dice[6]
    else:
        dice[6] =  board[x][y]
        board[x][y] = 0
    print(dice[1])

for i in do:
    check(i)