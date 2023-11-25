import sys
import heapq
v, e = map(int, sys.stdin.readline().rstrip().split())
# print(v)
st = int(input())
arr = [[] for _ in range(v+1)]
dist = [ 200001 for _ in range(v+1)]
for i in range(e):
    u,v2,w = map(int, sys.stdin.readline().rstrip().split())
    arr[u].append((v2,w))
# print(v)
heap =[]
heapq.heappush(heap, (0, st))
dist[st] = 0
while heap:
    distance, cur_v = heapq.heappop(heap)
    if dist[cur_v] != distance:
        continue
    for e,d in arr[cur_v]:
        if dist[e]> dist[cur_v] + d:
            dist[e] = dist[cur_v] + d
            heapq.heappush(heap, (dist[e],e))
# print(dist)
for i in range(1, v+1):
    if dist[i] == 200001:
        print("INF")
    else:
        print(dist[i])
    # print(v)
    # print(i, dist[i])