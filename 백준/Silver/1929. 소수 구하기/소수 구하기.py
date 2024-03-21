# 소수 = 1과 자기 자신만을 약수로 가지는 수

# 소수를 구하는 방법
# 1. 2부터 n-1까지 모두 나눠서 나눠지는 수가 없으면 소수이다. (시간 초과)
# 2. 2부터 n의 제곱근까지만 나눠서 나눠지는 수가 없으면 소수이다. (에라토스테네스의 체)
import sys
M, N = map(int, sys.stdin.readline().split())  # 사용자로부터 두 개의 숫자를 입력받아 M과 N에 저장


def eratosthenes(num):  # 소수 판별 함수
    if num == 1:  # 1은 소수가 아니므로 False 반환
        return False
    else:  # num을 2부터 num의 제곱근까지의 모든 숫자로 나눈다. 어떤 숫자로 나눠떨어진다면 num은 소수가 아니므로 False 반환
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True  # num이 소수인 경우


for i in range(M, N + 1):
    if eratosthenes(i):
        print(i)  # 소수인 경우 출력
