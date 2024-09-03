def solution(arr, k):
    answer = []
    if k % 2: # 홀수
        answer = [i * k for i in arr]
    else: # 짝수
        answer = [i + k for i in arr]
    return answer