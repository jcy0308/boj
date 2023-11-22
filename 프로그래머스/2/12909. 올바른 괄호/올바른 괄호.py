def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False
    if len(stack) == 0:
        return True
    return False