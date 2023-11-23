visit = [0 for x in range(8)]
count = 0
def solution(k, dungeons):
    global count
    bt(k, dungeons, 0)
    return count
def bt(value, dungeons, cnt):
    global visit
    global count
    for idx, dungeon in enumerate(dungeons):
        if visit[idx] == 0 and value-dungeon[0]>=0:
            visit[idx] = 1
            bt(value-dungeon[1], dungeons, cnt+1)
            visit[idx] = 0
    count = max(count, cnt)
    return 