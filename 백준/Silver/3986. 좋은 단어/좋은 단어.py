n = int(input())
count = 0

for _ in range(n):
    word = input()
    stack = []

    for char in word:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        count += 1

print(count)