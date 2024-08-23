def solution(num_list, n):
    a_list = num_list[:n]
    b_list = num_list[n:]
    answer = b_list+a_list
    return answer