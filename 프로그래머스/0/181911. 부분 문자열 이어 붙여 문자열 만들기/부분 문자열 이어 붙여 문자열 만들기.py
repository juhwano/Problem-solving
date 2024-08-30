def solution(my_strings, parts):
    answer = []
    for string, part in zip(my_strings, parts):
        answer.append(string[part[0]:part[1]+1])
    answer = ''.join(answer)
    
    return answer