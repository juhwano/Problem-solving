def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        slice_arr = int(str[s:s+l])
        if slice_arr > k:
            answer.append(slice_arr)
    
    return answer