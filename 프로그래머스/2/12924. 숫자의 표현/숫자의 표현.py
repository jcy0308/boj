def solution(n):
    answer = 1
    for i in range(2,n):
        s,e = (1,i)
        subsum = (e**2+e)/2 # 1+2
        # print(subsum)
        while e < n:
            if subsum == n:
                answer += 1
                break
            elif subsum > n:
                break
            e = e+1
            subsum -= s
            subsum += e
            s = s+1
    return answer