def solution(ineq, eq, n, m):
    answer = 0
    if ineq ==">" and n > m:
        answer = 1
    elif ineq == "<" and n < m:
        answer = 1
    elif eq == "=" and n == m:
        answer = 1

    return answer
