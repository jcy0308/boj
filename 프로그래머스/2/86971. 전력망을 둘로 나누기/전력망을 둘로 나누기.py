from collections import deque

def solution(n, wires):
    answer = 101
    def bfs(idx):
        visited = [0 for x in range(n+1)]
        count = 1
        root_num = wires[0][0]
        que = deque()
        que.append(root_num)
        visited[root_num] = 1
        while len(que):
            cur = que.popleft()
            for i, wire in enumerate(wires):
                if i == idx:
                    continue
                if wire[0] == cur and visited[wire[1]] == 0:
                    visited[wire[1]] = 1
                    count += 1
                    que.append(wire[1])
                if wire[1] == cur and visited[wire[0]] == 0:
                    visited[wire[0]] = 1
                    count += 1
                    que.append(wire[0])
        return count 
    for idx, wire in enumerate(wires):
        size = bfs(idx)
        print(size)
        diff = abs((n-size) - size)
        if diff < answer:
            answer = diff
    return answer