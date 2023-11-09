def solution(genres, plays):
    answer = []
    dic = {}
    for idx, genre in enumerate(genres):
        if genre in dic:
            dic[genre][0] += plays[idx]
            if len(dic[genre][1]) == 1:
                if plays[idx] > plays[dic[genre][1][0]]:
                    dic[genre][1].insert(0,idx)
                elif plays[idx] == plays[dic[genre][1][0]]:
                    dic[genre][1].append(idx) 
                    dic[genre][1].sort()
                else:
                    dic[genre][1].append(idx)      
            else: #len ==2
                if plays[idx] > plays[dic[genre][1][0]]:
                    dic[genre][1].pop(-1)
                    dic[genre][1].insert(0,idx)
                elif plays[idx] > plays[dic[genre][1][1]] or plays[idx] == plays[dic[genre][1][0]]:
                    dic[genre][1].pop(-1)
                    dic[genre][1].append(idx)    
        else:
            dic[genre] = [plays[idx], [idx]]
    ranks = sorted(dic.items(), key= lambda x: x[1][0], reverse=True)
    print(ranks)
    for rank in ranks:
        answer+=rank[1][1]
    return answer