def solution(n):
    n = str(n)  # 정수 n을 문자열로 변환합니다.
    sorted_digits = sorted(n, reverse=True)  # n의 각 자릿수를 내림차순으로 정렬합니다.
    sorted_n = ''.join(sorted_digits)  # 정렬된 자릿수를 이어붙여 새로운 문자열로 만듭니다.
    return int(sorted_n)  # 문자열을 정수로 변환하여 반환합니다.