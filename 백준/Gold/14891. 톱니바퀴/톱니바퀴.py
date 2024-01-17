chain = []
for i in range(4):
    chain.append(list(map(int,list(input()))))
# print(chain)
def move(num, dir):
    if dir == 0:
        return
    global chain
    if dir == -1: #반시계
        chain[num].append(chain[num].pop(0))
    else: #시계
        chain[num].insert(0, chain[num].pop(-1))

def check(s,d):
    global tmp
    if s == 1:
        tmp[0] = d
        if chain[0][2] != chain[1][6]:
            tmp[1] = -d
            if chain[1][2] != chain[2][6]:
                tmp[2] = -tmp[1]
                if chain[2][2] != chain[3][6]:
                    tmp[3] = -tmp[2]
    elif s == 2:
        tmp[1] = d
        if chain[0][2] != chain[1][6]:
            tmp[0] = -d
        if chain[1][2] != chain[2][6]:
            tmp[2] = -d
            if chain[2][2] != chain[3][6]:
                tmp[3] = -tmp[2]
    elif s ==3:
        tmp[2] = d
        if chain[3][6] != chain[2][2]:
            tmp[3] = -d
        if chain[2][6] != chain[1][2]:
            tmp[1] = -d
            if chain[0][2] != chain[1][6]:
                tmp[0] = -tmp[1]
    else:
        tmp[3] = d     
        if chain[3][6] != chain[2][2]:
            tmp[2] = -d
            if chain[1][2] != chain[2][6]:
                tmp[1] = -tmp[2]
                if chain[0][2] != chain[1][6]:
                    tmp[0] = -tmp[1]           
n = int(input())
for i in range(n):
    tmp = [0,0,0,0] #1은 시계, -1 은 반시계
    src, dir = map(int, input().split())
    check(src,dir)
    # print(tmp)
    for i in range(4):
        move(i,tmp[i])
    # for i in range(4):
    #     print(chain[i])
print(chain[0][0]+chain[1][0]*2+chain[2][0]*4+chain[3][0]*8)
    