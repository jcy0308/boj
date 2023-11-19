def parametric_search(n,threshold,arr):
    count = 0 
    for item in arr:
        count += n//item
    if count >= threshold:
        return True
    return False
def solution(n, times):
    lower_bound, upper_bound = (1, 10000000000000000000)
    while lower_bound < upper_bound:
        mid = (lower_bound+upper_bound)//2
        if parametric_search(mid, n, times):
            upper_bound = mid
        else:
            lower_bound = mid+1
        # print(lower_bound, upper_bound)
    return lower_bound
    # return parametric_search(29,28,times)