def solution(s):
    return ''.join(sorted(s, reverse=True))

# sorted(s, reverse=True) : s 상자 안에 있는 단어나 문장을 가장 큰 글자부터 가장 작은 글자 순서로 바꿉니다. 예를 들어, "abc"는 "cba"로 바뀝니다.
# reverse는 매개변수는 정렬 순서를 결정합니다. 기본값은 False
# True로 설정하면 내림차순(큰 것부터 작은 것 순서)로 정렬합니다.

# 예를 들어
# [3, 1, 4, 1, 5, 9]라는 리스트를 
# sorted() 함수로 정렬하면 [1, 1, 3, 4, 5, 9]가 됩니다. 
# 하지만 reverse=True를 설정하면 [9, 5, 4, 3, 1, 1]이 됩니다.
