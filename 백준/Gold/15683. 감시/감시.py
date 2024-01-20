import sys
n, m = map(int, sys.stdin.readline().strip().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
used = [[0 for x in range(m)] for y in range(n)]
checked = [[0 for x in range(m)] for y in range(n)]
count = 9999
def fill(x,y,dir):
    global arr, checked
    if dir == 0:
        x = x -1
        while x >= 0:
            if arr[x][y] == 6:
                break
            if arr[x][y] ==0 and checked[x][y]== 0:
                arr[x][y] = '#'
                checked[x][y] += 1
            elif checked[x][y] >= 1 and arr[x][y] == '#':
                checked[x][y] += 1
            x -= 1
    elif dir == 1:
        y += 1
        while y < m:
            if arr[x][y] == 6:
                break
            if arr[x][y] == 0 and checked[x][y]== 0:
                arr[x][y] = '#'
                checked[x][y] += 1
            elif checked[x][y] >= 1 and arr[x][y] == '#':
                checked[x][y] += 1
            y += 1
    elif dir == 2:
        x += 1
        while x < n:
            if arr[x][y] == 6:
                break
            if arr[x][y] == 0 and checked[x][y]== 0:
                arr[x][y] = '#'
                checked[x][y] += 1
            elif checked[x][y] >= 1 and arr[x][y] == '#':
                checked[x][y] += 1
            x += 1
    elif dir == 3:
        y -= 1
        while y >= 0:
            if arr[x][y] == 6:
                break
            if arr[x][y] == 0 and checked[x][y]== 0:
                arr[x][y] = '#'
                checked[x][y] += 1
            elif checked[x][y] >= 1 and arr[x][y] == '#':
                checked[x][y] += 1
            y -= 1
def unfill(x,y,dir):
    global checked, arr
    if dir == 0:
        x = x -1
        while x >= 0:
            if arr[x][y] == 6:
                break
            if checked[x][y] >= 2:
                checked[x][y] -= 1
            elif checked[x][y] == 1:
                checked[x][y] -= 1
                arr[x][y] = 0
            x -= 1
    elif dir == 1:
        y += 1
        while y <m:
            if arr[x][y] == 6:
                break
            if checked[x][y] >= 2:
                checked[x][y] -= 1
            elif checked[x][y] == 1:
                checked[x][y] -= 1
                arr[x][y] = 0
            y += 1
    elif dir == 2:
        x += 1
        while x < n:
            if arr[x][y] == 6:
                break
            if checked[x][y] >= 2:
                checked[x][y] -= 1
            elif checked[x][y] == 1:
                checked[x][y] -= 1
                arr[x][y] = 0
            x += 1
    elif dir == 3:
        y -= 1
        while y >= 0:
            if arr[x][y] == 6:
                break
            if checked[x][y] >= 2:
                checked[x][y] -= 1
            elif checked[x][y] == 1:
                checked[x][y] -= 1
                arr[x][y] = 0
            y -= 1
def cctv(num, x,y,dir):
    global arr
    if num == 1:
        if dir == 0: #북
            fill(x,y,0)
        elif dir == 1:
            fill(x,y,1)
        elif dir == 2:
            fill(x,y,2)
        elif dir == 3:
            fill(x,y,3)
    elif num == 2:
        if dir == 0: #북
            fill(x,y,0)
            fill(x,y,2)
        elif dir == 1:
            fill(x,y,1)
            fill(x,y,3)
        elif dir == 2:
            fill(x,y,0)
            fill(x,y,2)
        elif dir == 3:
            fill(x,y,1)
            fill(x,y,3)
    elif num == 3:
        if dir == 0: #북
            fill(x,y,0)
            fill(x,y,1)
        elif dir == 1:
            fill(x,y,1)
            fill(x,y,2)
        elif dir == 2:
            fill(x,y,2)
            fill(x,y,3)
        elif dir == 3:
            fill(x,y,3)
            fill(x,y,0)
    elif num == 4:
        if dir == 0: #북
            fill(x,y,0)
            fill(x,y,1)
            fill(x,y,3)
        elif dir == 1:
            fill(x,y,1)
            fill(x,y,0)
            fill(x,y,2)
        elif dir == 2:
            fill(x,y,1)
            fill(x,y,2)
            fill(x,y,3)
        elif dir == 3:
            fill(x,y,0)
            fill(x,y,3)
            fill(x,y,2)
    elif num == 5:
        fill(x,y,0)
        fill(x,y,1)
        fill(x,y,2)
        fill(x,y,3)


def clear(num, x,y,dir):
    global arr
    if num == 1:
        if dir == 0: #북
            unfill(x,y,0)
        elif dir == 1:
            unfill(x,y,1)
        elif dir == 2:
            unfill(x,y,2)
        elif dir == 3:
            unfill(x,y,3)
    elif num == 2:
        if dir == 0: #북
            unfill(x,y,0)
            unfill(x,y,2)
        elif dir == 1:
            unfill(x,y,1)
            unfill(x,y,3)
        elif dir == 2:
            unfill(x,y,0)
            unfill(x,y,2)
        elif dir == 3:
            unfill(x,y,1)
            unfill(x,y,3)
    elif num == 3:
        if dir == 0: #북
            unfill(x,y,0)
            unfill(x,y,1)
        elif dir == 1:
            unfill(x,y,1)
            unfill(x,y,2)
        elif dir == 2:
            unfill(x,y,2)
            unfill(x,y,3)
        elif dir == 3:
            unfill(x,y,3)
            unfill(x,y,0)
    elif num == 4:
        if dir == 0: #북
            unfill(x,y,0)
            unfill(x,y,1)
            unfill(x,y,3)
        elif dir == 1:
            unfill(x,y,1)
            unfill(x,y,0)
            unfill(x,y,2)
        elif dir == 2:
            unfill(x,y,1)
            unfill(x,y,2)
            unfill(x,y,3)
        elif dir == 3:
            unfill(x,y,0)
            unfill(x,y,3)
            unfill(x,y,2)
    elif num == 5:
        unfill(x,y,0)
        unfill(x,y,1)
        unfill(x,y,2)
        unfill(x,y,3)
def bt(x,y):
    global count, arr, used,n,m
    if x==n-1 and y==m-1 and used[x][y] == 1:
        tmp = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    tmp += 1
        if count > tmp:
            count = tmp
            # for k in range(n):
            #     print(checked[k])  
            # print()
            # for k in range(n):
            #     print(arr[k])  
            # print()
            # for k in range(n):
            #     print(used[k]) 
            # print()
        return
    
    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == 5:
                cctv(5,i,j,0)
            if i==n-1 and j==m-1:
                if arr[i][j] not in [1,2,3,4]:
                    tmp = 0
                    for k in range(n):
                        for l in range(m):
                            if arr[k][l] == 0:
                                tmp += 1
                    # count = min(count, tmp)
                    if count > tmp :
                        count = tmp
                        # for k in range(n):
                        #     print(checked[k]) 
                        # print()
                        # for k in range(n):
                        #     print(checked[k])  
                        # print()
                        # for i in range(n):
                        #     print(used[i]) 
                        # print() 
                    return
            if used[i][j] == 1 or arr[i][j] == 0 or arr[i][j] == 6 or arr[i][j] == '#':
                continue
            if arr[i][j] == 1:
                cctv(1,i,j,0)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(1,i,j,0)
                
                cctv(1,i,j,1)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(1,i,j,1)
                
                cctv(1,i,j,2)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(1,i,j,2)
                
                cctv(1,i,j,3)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(1,i,j,3)
                return
            elif arr[i][j] == 2:
                cctv(2,i,j,0)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(2,i,j,0)
                
                cctv(2,i,j,1)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(2,i,j,1)
                return
            
            elif arr[i][j] == 3:
                cctv(3,i,j,0)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(3,i,j,0)
                
                cctv(3,i,j,1)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(3,i,j,1)
                
                cctv(3,i,j,2)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(3,i,j,2)
                
                cctv(3,i,j,3)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(3,i,j,3)
                return
            
            elif arr[i][j] == 4:
                cctv(4,i,j,0)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(4,i,j,0)
                
                cctv(4,i,j,1)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(4,i,j,1)
                
                cctv(4,i,j,2)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(4,i,j,2)
                
                cctv(4,i,j,3)
                used[i][j] = 1
                bt(i,j)
                used[i][j] = 0
                clear(4,i,j,3)
                return
                
            # elif arr[i][j] == 5:
            #     cctv(5,i,j,0)
            #     used[i][j] = 1
            #     # bt(i,j)
            #     # used[i][j] = 0
            #     # clear(5,i,j,0)
            #     return

bt(0,0)
print(count)

# test = [arr_[:] for arr_ in arr]
# cctv(1,0,0,1)
# cctv(1,1,1,1)
# cctv(1,2,2,1)
# cctv(5,2,3,0)
# cctv(5,3,2,0)
# cctv(1,3,3,3)
# cctv(1,4,4,3)
# cctv(1,5,5,3)
# clear(1,5,5,3)
# clear(1,4,4,3)
# clear(1,3,3,3)
# clear(5,3,2,0)
# clear(5,2,3,0)
# clear(1,2,2,1)
# clear(1,1,1,1)
# clear(1,0,0,1)
