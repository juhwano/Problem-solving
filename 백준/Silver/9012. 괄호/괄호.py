import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    vps = input().strip()
    stack = []
    for i in vps:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')