import sys
input = sys.stdin.readline
numbers = list(map(int, input().split()))
sum = 0

for i in numbers:
    sum += i

print(sum)
