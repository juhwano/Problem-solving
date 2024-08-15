def solution(num_list):
    # 이해,목표
    # - 정수 리스트의 모든 곱 < 모든 합의 제곱 : 1
    # - 정수 리스트의 모든 곱 > 모든 합의 제곱 : 1
    # 시간복잡도, 공간복잡도
    # - O(n)
    
    모든곱=1
    for i in num_list:
        모든곱 *= i
    합의제곱 = sum(num_list)**2
    
    return 1 if 모든곱 < 합의제곱 else 0