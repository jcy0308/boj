tmp = ["ICN"]
def solution(tickets):
    answer = []
    used =  [0 for x in range(len(tickets))]
    def bt(answer):
        global tmp
        if len(tmp) == len(tickets)+1:
            real = tmp[:]
            answer.append(real)
            # print(tmp)
            return
        for idx, (src, dec) in enumerate(tickets):
            if src == tmp[-1] and used[idx] == 0:
                used[idx] = 1
                tmp.append(dec)
                # print(tmp)
                bt(answer)
                used[idx] = 0
                tmp.pop()
    for idx, (src, dec) in enumerate(tickets):
        if src == "ICN":
            used[idx] = 1
            tmp.append(dec)
            # print(tmp)
            bt(answer)
            used[idx] = 0
            tmp.pop()
    return min(answer)