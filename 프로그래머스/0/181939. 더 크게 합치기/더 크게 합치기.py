def solution(a, b):
    str_a=str(a)
    str_b=str(b)
    str_ab=str_a+str_b
    str_ba=str_b+str_a
    int_ab= int(str_ab)
    int_ba= int(str_ba)
    answer = int_ab if int_ab > int_ba else int_ba
    return answer