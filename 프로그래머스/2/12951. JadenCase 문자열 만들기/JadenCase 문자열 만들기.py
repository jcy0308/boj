def solution(s):
    tmp = s.split(' ')
    answer = ''
    tmp2 = []
    for string in tmp:
        tmp2.append(string.capitalize())
    answer = ' '.join(tmp2)
    return answer