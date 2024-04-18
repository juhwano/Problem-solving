def solution(cards1, cards2, goal):
    index1, index2 = 0, 0  # cards1, cards2의 현재 인덱스
    for word in goal:
        if index1 < len(cards1) and cards1[index1] == word:
            index1 += 1
        elif index2 < len(cards2) and cards2[index2] == word:
            index2 += 1
        else:
            return 'No'  # goal의 단어를 찾지 못한 경우

    return 'Yes'  # 모든 goal의 단어를 찾은 경우