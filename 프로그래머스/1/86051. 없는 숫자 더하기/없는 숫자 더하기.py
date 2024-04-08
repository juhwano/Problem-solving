def solution(numbers):
    # 체크 리스트
    check_list = [i for i in range(10)]
    # 반환 결과
    result = []
    
    for i in check_list:
        if i not in numbers:
            result.append(i)
    
    return sum(result)