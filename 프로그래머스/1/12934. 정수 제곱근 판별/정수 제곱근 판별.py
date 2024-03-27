def solution(n):
    if n == int(n ** 0.5) ** 2:
        answer = int((n ** 0.5) + 1) ** 2
    else:
        answer = -1
    return answer