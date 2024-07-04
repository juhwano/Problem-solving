hour, minute = map(int,input().split())
addTime = int(input())
totalMinute = hour * 60 + minute + addTime

if totalMinute >= 1440:
  totalMinute -= 1440

hour = totalMinute // 60
minute=totalMinute % 60
print(f"{hour} {minute}")