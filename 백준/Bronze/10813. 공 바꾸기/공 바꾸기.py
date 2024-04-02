# 카드의 개수 N과 섞는 횟수 M을 입력받습니다.
N, M = map(int, input().split())
# 1부터 N까지의 번호가 적힌 카드를 준비합니다.
cards = [i for i in range(1, N+1)]
# M번 섞는 작업을 수행합니다.
for _ in range(M):
    # 섞는 방법을 입력받습니다. 카드 번호가 1부터 시작하므로, 리스트의 인덱스로 사용하기 위해 1을 빼줍니다.
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    # i번 카드와 j번 카드의 위치를 바꿉니다.
    cards[i], cards[j] = cards[j], cards[i]
# 모든 카드를 출력합니다.
for card in cards:
    print(card, end=' ')
