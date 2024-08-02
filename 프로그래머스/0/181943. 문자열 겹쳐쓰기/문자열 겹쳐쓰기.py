def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

# 6 반례입니다.
# 입력값 〉 "aaaaaa", "bbb", 3
# 기댓값 〉 "aaabbb"