import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
for char in A:
    if char < X:
        print(char, end=' ')
