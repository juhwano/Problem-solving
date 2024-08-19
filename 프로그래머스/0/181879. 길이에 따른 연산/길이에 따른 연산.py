def solution(num_list):
    list_length = len(num_list)
    mul=1
    if list_length >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            mul *= i
        return mul