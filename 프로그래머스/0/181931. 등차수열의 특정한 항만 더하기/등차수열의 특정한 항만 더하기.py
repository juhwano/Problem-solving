def solution(a, d, included):
    # 등차수열의 일반항
    # An = A1 + B(n-1)
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer