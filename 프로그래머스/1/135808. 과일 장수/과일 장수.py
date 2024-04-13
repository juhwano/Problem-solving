from collections import deque

def solution(k, m, score):
    max_benefit = 0
    score.sort(reverse=True)  # score 리스트를 내림차순으로 정렬합니다.
    score = deque(score)  # score 리스트를 deque로 변환합니다.
    while len(score) >= m:
        box = [score.popleft() for _ in range(m)]  # 가장 값이 큰 m개의 사과를 한 번에 선택하고 제거합니다.
        min_value_apple = min(box)
        max_benefit += min_value_apple * m
    return max_benefit