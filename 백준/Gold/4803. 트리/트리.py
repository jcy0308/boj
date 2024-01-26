from collections import deque

def bfs(st, edges):
    global used
    # used = [-1 for _ in range(n+1)]
    # pool = []
    q = deque()
    q.append(st)
    # pool.append(st)
    flag = True
    used[st] = st #루트의 부모는 자기 자신
    while q:
        cur = q.popleft()
        for v in edges[cur]:
            if used[v] == -1:
                used[v] = cur
                # pool.append(v)
                q.append(v)
            elif v == used[cur]:
                continue
            else:
                flag = False
    return flag
                
testcase = 1
while True:
    n, m = map(int, input().split())
    if n==0 and m == 0:
        break
    used = [-1 for x in range(n+1)]
    edges = [[] for _ in range(n+1)]
    for i in range(m):
        st, en = map(int, input().split())
        edges[st].append(en)
        edges[en].append(st)
    cnt = 0
    for i in range(1,n+1):
        if used[i] == -1:
            cnt += bfs(i, edges)
    if cnt == 0: 
        print("Case {:d}: No trees.".format(testcase))
    elif cnt == 1:
        print("Case {:d}: There is one tree.".format(testcase))
    else:
        print("Case {:d}: A forest of {:d} trees.".format(testcase, cnt))
    testcase += 1
    
        
        