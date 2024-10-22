def solution(array):
    answer = sorted(array, key=lambda x:x)
    mid_index = len(answer)//2
    result = answer[mid_index]
    return result