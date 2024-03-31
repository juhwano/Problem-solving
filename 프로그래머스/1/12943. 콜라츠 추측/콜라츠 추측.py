def solution(num, count=0):  # num은 주어진 숫자, count는 연산을 반복한 횟수입니다.
    if num == 1:  # 만약 숫자가 1이라면,
        return count  # 연산을 반복한 횟수를 반환합니다.
    elif count == 500:  # 만약 연산을 500번 반복했다면,
        return -1  # -1을 반환합니다.
    elif num % 2 == 0:  # 만약 숫자가 짝수라면,
        return solution(num / 2, count + 1)  # 숫자를 2로 나눈 후, 연산을 반복한 횟수를 1 증가시키고 재귀 호출합니다.
    else:  # 만약 숫자가 홀수라면,
        return solution(num * 3 + 1, count + 1)  # 숫자에 3을 곱하고 1을 더한 후, 연산을 반복한 횟수를 1 증가시키고 재귀 호출합니다.