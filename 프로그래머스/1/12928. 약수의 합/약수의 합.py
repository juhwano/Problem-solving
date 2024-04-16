def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:  # i가 n의 약수인 경우
            answer += i  # 약수를 더합니다.
    return answer