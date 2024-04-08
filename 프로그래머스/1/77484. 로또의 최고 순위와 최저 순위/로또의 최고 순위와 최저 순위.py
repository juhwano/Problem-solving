def solution(lottos, win_nums):
    # 0 개수 확인(0~4)
    # 현재 당첨 번호 개수 확인(2~6)
    # 순위 매칭
    # 출력
    win_count = 0
    zero_count = lottos.count(0) # 0 개수 확인
    
    for i in lottos:
        if i in win_nums:
            win_count += 1 # 현재 당첨 번호 개수 확인
    
    max_ranking = 7 - max(win_count + zero_count, 1) # 합쳐서 6
    min_ranking = 7 - max(win_count, 1)
    
    return [max_ranking, min_ranking]