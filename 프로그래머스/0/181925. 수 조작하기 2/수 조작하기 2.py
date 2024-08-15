def solution(numLog):
    
    answer=''
    for num in range(len(numLog)):
        if num == 0:
            continue
        else:
            if numLog[num] - numLog[num-1] == 1:
                answer+='w'
            elif numLog[num] - numLog[num-1] == -1:
                answer+='s'
            elif numLog[num] - numLog[num-1] == 10:
                answer+='d'
            else:
                answer+='a'
            
    return answer
            