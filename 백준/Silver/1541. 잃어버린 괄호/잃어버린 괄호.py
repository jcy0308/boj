line = input()
numbers = []
symbols = []
tmp = ''
for letter in line:
    if letter in ['-','+']:
        numbers.append(int(tmp))
        symbols.append(letter)
        tmp = ''
    else:
        tmp += (letter)
numbers.append(int(tmp))
# print(numbers)
# print(symbols)
answer = numbers[0]
# for number in numbers[1:]:
cursor = 1
flag = 0
for i in symbols:
    if flag == 1:
        if i == '-':
            answer -= numbers[cursor]
        elif i == '+':
            answer -= numbers[cursor]
    else:
        if i == '+':
            answer += numbers[cursor]
        elif i == '-':
            answer -= numbers[cursor]
            flag = 1
    cursor += 1
print(answer)
        
    