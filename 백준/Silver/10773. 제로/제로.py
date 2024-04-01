import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    i = int(input())
    if i == 0:
        if len(stack) != 0:
            stack.pop()
        else:
            continue
    else:
        stack.append(i)

result = 0
for i in stack:
    result += i

print(result)
