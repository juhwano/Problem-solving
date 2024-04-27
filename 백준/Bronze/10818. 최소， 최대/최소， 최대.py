import sys
input = sys.stdin.readline

N = input()
numbers = list(map(int,input().split()))
max = -sys.maxsize - 1  # 가능한 가장 작은 수로 초기화
min = sys.maxsize  # 가능한 가장 큰 수로 초기화
for number in numbers:
    if number > max:
        max = number
    if number < min:
        min = number

print(str(min) + ' ' + str(max))