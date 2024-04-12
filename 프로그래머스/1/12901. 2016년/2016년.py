def solution(a, b):
    days = ['FRI', 'SAT', 'SUN','MON', 'TUE', 'WED', 'THU']
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum_days = 0
    for i in range(a-1):
        sum_days += months[i]
    sum_days += b
    target_day = sum_days % 7 - 1
    answer = days[target_day]

    return answer