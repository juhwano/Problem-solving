import sys
from collections import deque

input = sys.stdin.readline
N = int(input())  # 카드의 개수를 입력받습니다.
li = list(map(int, sys.stdin.readline().split()))  # 사용한 기술들을 입력받습니다. 이때, map 함수를 사용하여 입력받은 문자열을 정수로 변환하고, list 함수를 사용하여 리스트로 변환합니다.
li.reverse()  # 리스트를 뒤집습니다. 이렇게 하면 기술들을 역순으로 적용할 수 있습니다.

dq = deque()  # 덱을 생성합니다.
for i in range(N):  # N번 반복합니다. 이때, i는 현재 카드의 번호입니다.
    if li[i] == 1:  # 만약 1번 기술을 사용했다면,
        dq.appendleft(i + 1)  # 덱의 왼쪽에 카드를 추가합니다. 이때, i + 1을 사용하여 카드의 번호를 1부터 시작하게 합니다.
    elif li[i] == 2:  # 만약 2번 기술을 사용했다면,
        dq.insert(1, i + 1)  # 덱의 두 번째 위치에 카드를 추가합니다. 이때, insert 함수를 사용하여 특정 위치에 카드를 추가합니다.
    elif li[i] == 3:  # 만약 3번 기술을 사용했다면,
        dq.append(i + 1)  # 덱의 오른쪽에 카드를 추가합니다.

for i in dq:  # 덱에 있는 카드들을 출력합니다.
    print(i, end=" ")  # print 함수를 사용하여 카드를 출력합니다. 이때, end=" "를 사용하여 카드를 한 줄에 출력하게 합니다.