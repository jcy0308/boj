from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    visited = [0 for x in range(len(words))]
    q.append(begin)
    while len(q):
        cur = q.popleft()
        for idx, word in enumerate(words):
            if compare(cur, word) == True and visited[idx] == 0:
                visited[idx] = visited[cur] + 1
                q.append(word)
    return answer
def compare(cur, word):
    cnt = 0
    for i in range(len(cur)):
        if cur[i] == word[i]:
            cnt +=1
    if cnt+1 == len(cur):
        return True
    return False
        