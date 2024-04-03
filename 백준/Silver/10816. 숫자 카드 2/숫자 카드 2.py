import sys
input = sys.stdin.readline

cards = {}
result = []
N = int(input())

N_list = list(map(int, input().split()))

for i in N_list:
    cards[i] = cards.get(i, 0) + 1

M = int(input())
M_list = list(map(int, input().split()))

for j in M_list:
    result.append(cards.get(j, 0))

for _ in result:
    print(_, end=' ')
