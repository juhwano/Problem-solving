import sys

left_stack = list(sys.stdin.readline().strip())
right_stack = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[2])

print(''.join(left_stack + right_stack[::-1]))