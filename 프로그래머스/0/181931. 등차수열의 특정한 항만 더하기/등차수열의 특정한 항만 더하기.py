def solution(a, d, included):
    # 등차수열의 일반항
    # An = A1 + B(n-1)
    sum = 0
    # 항수를 알아야한다.
    for i, bool in enumerate(included):
        if bool == True:
            sum += a + i * d

    return sum