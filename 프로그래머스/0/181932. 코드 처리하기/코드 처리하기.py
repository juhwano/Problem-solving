def solution(code):
    code_list = list(code)
    mode = 0
    rat = ''
    for i in range(len(code_list)):
        if mode == 0:
            if code_list[i] != '1' and i%2 ==0:
                rat += code_list[i]
            if code_list[i] == '1':
                mode = 1
        else:
            if code_list[i] != '1' and i%2 ==1:
                rat += code_list[i]
            if code_list[i] == '1':
                mode = 0
    if rat == '':
        return 'EMPTY'
    answer = rat
    return answer