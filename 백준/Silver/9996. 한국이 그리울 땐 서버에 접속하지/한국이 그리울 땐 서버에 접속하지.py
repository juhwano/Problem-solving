N = int(input())
pattern = input()
pattern = pattern.split('*')
# 내가 빠트린 부분
size = len(pattern[0]) + len(pattern[1])
for _ in range(N):
    fileName = input()
    if len(fileName) >= size and fileName.startswith(pattern[0]) and fileName.endswith(pattern[1]):
        print('DA')
    else:
        print('NE')
