# 사용자로부터 숫자의 개수 N을 입력받는다.
N = int(input())
# 숫자 N개를 문자열로 입력받는다.
numbers = input()
# 각 숫자를 정수로 변환하고 합산
total = sum(int(num) for num in numbers)
# 결과 출력
print(total)