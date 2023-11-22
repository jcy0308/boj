def solution(s):
    answer = [0,0]
    while s != '1':
    # for i in range(3):
        tmp ='' 
        for char in s:
            if char == '0':
                answer[1] += 1
            else:
                tmp += '1'
        answer[0] += 1
        p = len(tmp)
        # print(tmp)
        ss = ''
        while p != 1:
            r = p%2
            p = p//2
            if r == 0:
                ss += '0'
            else:
                ss += '1'
        ss += '1'
        s = ss[::-1]
        print(s)
    return answer