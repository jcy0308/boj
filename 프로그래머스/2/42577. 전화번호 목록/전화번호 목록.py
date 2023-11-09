def solution(phone_book):
    answer = True
    dic = dict()
    for number in phone_book:
        for i in range(1,len(number)):
            # if number[:i] in dic:
            #     answer = False
            #     print(dic)
            #     return answer
            dic[number[:i]] = 1
    for number in phone_book:
        if number in dic:
            answer = False
            return answer
    return answer