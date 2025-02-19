import math

a, b, v = map(int, input().split())

before_last_day = math.ceil((v - a) / (a - b))

total_day = before_last_day + 1

print(total_day)