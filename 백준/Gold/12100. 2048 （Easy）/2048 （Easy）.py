from collections import deque
n = int(input())
ans = 0
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# def compress():
    
def update(arr, dir):
    new_arr = [[ 0 for x in range(n)] for y in range(n)]
    if dir == 1:
        for i in range(n):
            tmp = []
            q = []
            for j in range(n):
                if arr[j][i] != 0:
                    q.append(arr[j][i])
            idx = 0
            while idx < len(q):
                # print(idx)
                if idx == len(q)-1:
                    tmp.append(q[idx])
                    break
                if q[idx] == q[idx+1]:
                    tmp.append(q[idx] *2)
                    idx += 1
                else:
                    tmp.append(q[idx])
                idx += 1
            for idx in range(len(tmp)):
                new_arr[idx][i] = tmp[idx]
    elif dir == 2:
        for i in range(n):
            tmp = []
            q = []
            for j in range(n-1,-1,-1):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
            idx = 0
            while idx < len(q):
                # print(idx)
                if idx == len(q)-1:
                    tmp.append(q[idx])
                    break
                if q[idx] == q[idx+1]:
                    tmp.append(q[idx] *2)
                    idx += 1
                else:
                    tmp.append(q[idx])
                idx += 1
            # print(tmp)
            for idx in range(len(tmp)):
                new_arr[i][n-1-idx] = tmp[idx]
    elif dir == 3:
        for i in range(n):
            tmp = []
            q = []
            for j in range(n-1,-1,-1):
                if arr[j][i] != 0:
                    q.append(arr[j][i])
            idx = 0
            while idx < len(q):
                # print(idx)
                if idx == len(q)-1:
                    tmp.append(q[idx])
                    break
                if q[idx] == q[idx+1]:
                    tmp.append(q[idx] *2)
                    idx += 1
                else:
                    tmp.append(q[idx])
                idx += 1
            for idx in range(len(tmp)):
                new_arr[n-1-idx][i] = tmp[idx]
    elif dir == 4:
        for i in range(n):
            tmp = []
            q = []
            for j in range(n):
                if arr[i][j] != 0:
                    q.append(arr[i][j])
            idx = 0
            while idx < len(q):
                # print(idx)
                if idx == len(q)-1:
                    tmp.append(q[idx])
                    break
                if q[idx] == q[idx+1]:
                    tmp.append(q[idx] *2)
                    idx += 1
                else:
                    tmp.append(q[idx])
                idx += 1
            for idx in range(len(tmp)):
                new_arr[i][idx] = tmp[idx]
    return new_arr
# print(update(board, 4))

def bt(arr, m):
    global ans
    if m == 5:
        
        # for i in range(n):
        #     print(arr[i])
        max_num = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > max_num:
                    max_num = arr[i][j]
        ans = max(max_num, ans)
        return
    
    for i in range(1,5):
        updated_arr = update(arr,i)
        bt(updated_arr,m+1)
    return

bt(board,0)
print(ans)
                
                