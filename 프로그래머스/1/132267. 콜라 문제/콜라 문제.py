def solution(a, b, n):
    answer = 0
    while n >= a:
        quotient, remainder = divmod(n, a)  # n을 a로 나누어, 몫과 나머지를 구함
        answer += quotient * b  # 새로 얻은 콜라 병의 수를 총량에 더함
        n = quotient * b + remainder  # 남은 병의 수를 업데이트함. 새 병과 남은 빈 병을 합침

    return answer  
