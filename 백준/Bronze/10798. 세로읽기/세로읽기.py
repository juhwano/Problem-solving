# 각 줄의 최대 길이는 15이므로, 15개의 공백으로 초기화된 리스트를 5개 만듭니다.
lines = [' ' * 15 for _ in range(5)]

# 5줄의 입력을 받습니다.
for i in range(5):
    line = input()
    # 입력받은 줄의 길이가 15보다 작을 경우, 남은 부분을 공백으로 채웁니다.
    lines[i] = line + ' ' * (15 - len(line))

# 세로로 읽어서 출력합니다.
for x in range(15):
    for y in range(5):
        # 공백이 아닌 문자만 출력합니다.
        if lines[y][x] != ' ':
            print(lines[y][x], end='')