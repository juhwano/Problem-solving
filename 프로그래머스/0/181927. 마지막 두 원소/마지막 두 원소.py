def solution(num_list):
    # 마지막 원소 기준
    # - 이전 원소와 값 비교
    # - 크면 뺀 값을 작으면 두배한 값을 마지막 인덱스에 추가한다.
    last = num_list[-1]
    before_last = num_list[-2]
    
    return num_list + [last - before_last] if before_last < last else num_list + [last*2]
    