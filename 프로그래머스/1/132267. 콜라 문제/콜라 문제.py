import sys

sys.setrecursionlimit(3000)

def solution(a, b, n):
    if n < a: return 0
    return b + solution(a, b, n-a+b) if n >= a else 0