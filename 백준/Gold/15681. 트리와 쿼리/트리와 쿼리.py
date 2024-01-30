n,r,q = map(int, input().split())
import sys
sys.setrecursionlimit(10**9)
arr= [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
size = [1 for _ in range(n+1)]
for _ in range(n-1):
    s,t = map(int, input().split())
    arr[s].append(t)
    arr[t].append(s)

parent[r] = 0
def subtree(arr, v):
    for next_node in arr[v]:
        if parent[next_node] == -1 and next_node != r:
            parent[next_node] = v
            size[v] += subtree(arr, next_node)
    return size[v]        
    
subtree(arr, r)
for _ in range(q):
    query = int(sys.stdin.readline())
    print(size[query])