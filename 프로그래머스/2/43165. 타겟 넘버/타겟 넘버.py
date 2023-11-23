from collections import deque
def solution(numbers, target):
    answer = 0
    answer += dfs(1, numbers[0], numbers, target)
    answer += dfs(1, -numbers[0], numbers, target)
    return answer

def dfs(idx, sum, numbers, target):
    if idx == len(numbers)-1:
        tmp = 0
        if target == sum+numbers[idx]:
            tmp += 1
        elif target == sum-numbers[idx]:
            tmp += 1
        return tmp
    return dfs(idx+1, sum+numbers[idx], numbers, target) +  dfs(idx+1, sum-numbers[idx], numbers, target)
