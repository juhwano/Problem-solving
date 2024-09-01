def solution(my_string):
    list_size= len(my_string)
    answer = []
    for i in range(1,list_size+1,1):
        answer.append(my_string[-i:])
    answer.sort()

    return answer