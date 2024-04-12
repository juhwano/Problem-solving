DAYS = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    # sum 함수를 사용하여 sum_days를 계산합니다.
    sum_days = sum(MONTHS[:a-1]) + b
    # sum_days를 7로 나눈 나머지를 사용하여 요일을 찾습니다.
    answer = DAYS[sum_days % 7]
    return answer