import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

cardList = []
for i in range(1, N+1):
    cardList.append(i)

data = deque(cardList)

while len(data) != 1:
    data.popleft()
    number = data.popleft()
    data.append(number)

for _ in data:
    print(_)
