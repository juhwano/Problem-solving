def solution(a, b, n):
    answer = 0
    while n >= a:
        quotient, remainder = divmod(n, a)
        answer += quotient * b
        n = quotient * b + remainder
    return answer