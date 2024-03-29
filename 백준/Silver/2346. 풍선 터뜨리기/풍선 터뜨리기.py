class Node:
    def __init__(self, data, prev=None, next=None):  # 객체 생성시 실행되는 함수
        self.data = data  # 저장되는 데이터
        self.prev = prev  # 이전 노드
        self.next = next  # 다음 노드


N = int(input())  # 풍선의 개수 N
balloon_numbers = list(map(int, input().split()))  # 풍선 안의 종이에 적혀 있는 수

# 링크드 리스트 생성
# 풍선 번호 1을 저장하는 노드 생성, head와 cur에 저장
head = Node(1)
cur = head
# 풍선 번호 2부터 N까지 각 노드를 생성하고, 이전 노드와 연결
for i in range(2, N+1):
    node = Node(i)  # 새 노드 생성
    node.prev = cur  # 새 노드의 이전 노드를 cur로 설정
    cur.next = node  # cur 노드의 다음 노드를 새 노드로 설정
    cur = node  # cur을 새 노드로 업데이트

cur.next = head  # 마지막 노드의 다음 노드를 head로 설정
head.prev = cur  # head의 이전 노드를 마지막 노드로 설정
# 풍선 터트리기
cur = head  # 현재 풍선 번호가 적힌 종이를 들고 있는 풍선
result = []

for i in range(N):
    result.append(cur.data)  # 터뜨린 풍선의 종이에 적힌 수를 결과에 추가
    step = balloon_numbers[cur.data-1]  # 풍선 안의 종이에 적힌 수만큼 이동
    if step > 0:  # 종이에 적혀 있는 수가 양수인 경우
        cur.prev.next = cur.next  # 터뜨린 풍선을 링크드 리스트에서 제거
        cur.next.prev = cur.prev  # 이전 노드와 다음 노드를 연결
        cur = cur.next  # 다음 풍선으로 이동
        # 종이에 적혀 있는 수만큼 오른쪽으로 이동
        for _ in range(step-1):
            cur = cur.next
    else:  # 종이에 적혀 있는 수가 음수인 경우
        cur.prev.next = cur.next  # 터뜨린 풍선을 링크드 리스트에서 제거
        cur.next.prev = cur.prev  # 이전 노드와 다음 노드를 연결
        cur = cur.prev  # 다음 풍선으로 이동
        # 종이에 적혀 있는 수만큼 왼쪽으로 이동
        for _ in range(abs(step)-1):
            cur = cur.prev

for i in result:
    print(i, end=' ') # 줄바꿈 대신 공백 출력
    
