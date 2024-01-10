from itertools import combinations


def find_distance(chicken, house):
    return abs(chicken[0]-house[0])+abs(chicken[1]-house[1])


n, m = map(int, input().split())
arr = [[]]
chic = []
for i in range(1, n+1):
    tmp = [0] + (list(map(int, input().split())))
    for j in range(1, n+1):
        if tmp[j] == 2:
            chic.append([i, j])
    arr.append(tmp)
# print(chic)
combos = combinations(chic, m)
ans = 999999
for combo in combos:
    # print(combo)
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] == 1:
                tmp_dis = 9999
                for k in combo:
                    new_dis = find_distance(k, (i,j))
                    # print(new_dis)
                    if tmp_dis > new_dis:
                        tmp_dis = new_dis
                cnt += tmp_dis
                # print(tmp_dis)
    if ans > cnt:
        ans = cnt
print(ans)
    

