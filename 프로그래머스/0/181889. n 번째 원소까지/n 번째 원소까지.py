def solution(num_list, n):
    answer = []
    for i, num in enumerate(num_list):
        if i > n-1:
            break
        else:
            answer.append(num)
    return answer