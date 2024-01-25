from collections import deque


n,w,l = map(int, input().split())
tmp= (list(map(int, input().split())))
trucks = deque()
for t in tmp :
    trucks.append(t)
# trucks = enumerate(list(map(int, input().split())))
st,en = 0,1
used = [0 for x in range(n)]
bridge = deque()
# first = trucks.popleft()
# bridge.append((first,w))  #(무게, 남은길이)
cur_w = 0
time = 0
while trucks or bridge:
    if trucks and l - cur_w >= trucks[0]:
        weight = trucks.popleft()
        bridge.append([weight,w])
        cur_w += weight
    for i in range(len(bridge)):
        bridge[i][1] -= 1
        # cur_w 
    while bridge and bridge[0][1] == 0:
        cur_w -= bridge.popleft()[0]
    time += 1 
    #print(bridge)
print(time+1)