def solution(arr, idx):
    answer = 0
    for i,v in enumerate(arr[idx:]):
        if v == 1:
            if idx+i == 0:
                answer = -2
                break
            else:
                answer = idx+i
                break
    if answer == 0:
        answer = -1
    if answer == -2:
        answer = 0
    return answer
        