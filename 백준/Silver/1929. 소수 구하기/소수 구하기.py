# 소수 = 1과 자기 자신만을 약수로 가지는 수

# 소수를 구하는 방법
# 1. 2부터 n-1까지 모두 나눠서 나눠지는 수가 없으면 소수이다. (시간 초과)
# 2. 2부터 n의 제곱근까지만 나눠서 나눠지는 수가 없으면 소수이다. (에라토스테네스의 체)
n, m = map(int, input().split())  # 사용자로부터 두 개의 숫자를 입력받아 n과 m에 저장

prime_list = [True]*(m+1)  # m+1 개의 True로 이루어진 리스트 생성
prime_list[0] = False  # 0은 소수가 아니므로 False로 변경
prime_list[1] = False  # 1은 소수가 아니므로 False로 변경

# 에라토스테네스의 체 알고리즘
# 2부터 N의 제곱근까지 반복(소수라면 그 숫자의 배수를 모두 소수가 아니라고 표시)
for i in range(2, int(m**0.5)+1):
    if prime_list[i]:
        for j in range(i*2, m+1, i):
            prime_list[j] = False

# M부터 N까지의 모든 숫자에 대해, 범위 내의 소수만 출력
for i in range(n, m+1):
    if prime_list[i]:
        print(i)
